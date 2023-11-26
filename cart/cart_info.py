import product.models
from product.models import Product


CART_SESSION_ID = 'cart'

# 3 -ایجاد یک کلید برای ذخیره سازی و دسترسی به اون محصول
class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID]= {}
        self.cart = cart



    def __iter__(self):
        cart = self.cart.copy()   # 9- اول از همه از اطلاعات سبد خرید یک کپی می گیریم
        for item in cart.values(): # 10 - میام روی آیتم های سبد خرید روی مقادیرشون حلقه فور می زنیم چونکه می خواییم یک سری کلید به اون اضافه کنیم
            product = Product.objects.get(id= int(item['id']))
            item['product'] = product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.unique_id_generator(product.id ,item['color'], item['size'])  #  Bبرای حذف محصول از سبد خرید به ایدی محصول نیاز داریم
            yield item


    def unique_id_generator(self,id,color,size): # 5- ایجاد متدی که ادی یونیک برای یک محصول بر اساس رنگ و سایز می سازد
        result =f'{id}-{color}-{size}'
        return result


    def add(self,product,quantity,size,color):  # 4-ایجاد یک متد برای اضافه کردن محصول به سبد خرید
        unique = self.unique_id_generator(product.id, color,size) # 6
        if unique not in self.cart: # چک می کنیم اگر اون ادی در داخل سبد خرید وجود نداشت یک دونه ایجاد می کنیم
            self.cart[unique] = {'quantity':0, 'price': str(product.price), 'color':color, 'size':size, 'id':product.id}
        self.cart[unique]['quantity'] += int(quantity) # اگر اون ادی وچود داشت فقط به تعدادش اضافه می کنیم
        self.save() # -8 تغییر ایجاد شده را با فراخوانی متد سیو ذخیره میکنیم


    # def total(self):  # متد قیمت کل محصولات انتخاب شده برای نشون دادن در جزئیات سبد خرید
    #     cart = self.cart.values()
    #     total = 0
    #     for item in cart:
    #         total += item['total']
    #     return total


    def total(self):  # متد قیمت کل محصولات انتخاب شده برای نشون دادن در جزئیات سبد خرید
        cart = self.cart.values() # آیتم ها ی سبد خرید
        total = sum(int(item['price']) * int(item['quantity']) for item in cart)
        return total

    def remove_cart(self): # ایجاد متد برای زمانی که کاربر ثبت سفارش می کند و به صفحه ی جزئیات اوردر هدایت می شود باید اطلاعات صحفه جزئیات کارت حذف شود
        del self.session[CART_SESSION_ID]

    def delete(self, id): # متد حذف محصول از سبد خرید که با ویویی که برای این منظور ایجاد کرده بودیم کار می کند C
        if id in self.cart:
            del self.cart[id]
            self.save()


    def save(self): # -7
        self.session.modified = True # زمانی که بخوایم توی اطلاعات مربوط به سشن هامون تغییری ایجاد کنیم باید
