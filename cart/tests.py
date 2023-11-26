# from django.shortcuts import render, get_object_or_404, redirect
# from django.test import TestCase
#
# # Create your tests here.
# from django.views import View
#
# from product.models import Product
#
#
# class CartDetail(View):
#     def get(self,request):
#         return render(request, 'cart/cart_detail.html', context={})
#
#
# class CartAddView(View):
#     def post(self,request,pk):
#         product = get_object_or_404(Product, id=pk)
#         size,color,quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
#         print(size,color,quantity, product)
#         return redirect('cart:cart_detail')
#
#
#
# class Cart:
#     def __init__(self,request):
#         self.session = request.session
#         cart = self.session.get('cart')
#         if not cart:
#             cart = self.session['cart']= {}
#         self.cart = cart
#
#
#     def unique_id_generator(self,id,color,size):
#         result = f'{id}-{color}-{size}'
#         return result
#
#
#     def add(self,product,quantity,size,color):
#         unique = self.unique_id_generator(product.id,color,size)
#         if unique not in self.cart:
#             self.cart[unique]= {'quantity':0, 'price':str(product.price), 'color':color, 'size':size, 'id':product.id}
#         self.cart[unique]['quantity'] += int(quantity)
#         self.save()
#
#
#
#     def save(self):
#         self.session.modified = True
#
#
