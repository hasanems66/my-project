from django.db import models
from math import ceil
from django.utils.html import format_html
from django.urls import reverse
# Create your models here.

class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    percentage_discount = models.SmallIntegerField(default=0)
    off_price = models.SmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product/images')
    size = models.ManyToManyField(Size, related_name='products')
    color = models.ManyToManyField(Color, related_name='products')
    slug = models.SlugField(blank=True, allow_unicode=True)
    status = models.BooleanField(default=True)
    published = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:product_detail', kwargs={'slug':self.slug})


    def percent_discount(self):
        if self.percentage_discount:
            percentage_discount = self.percentage_discount
            multiplier = percentage_discount /100
            old_price = self.price
            new_price = ceil(old_price - (old_price * multiplier))
            self.off_price = new_price
            
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields='off_price'):
        self.percent_discount()
        super(Product, self).save()


    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="55px">')
        return format_html('<p class="text-red">تصویری ندارد<p>')


class Information(models.Model):
    product = models.ForeignKey(Product,null=True, on_delete=models.CASCADE, related_name='informations')
    text = models.TextField()


    def __str__(self):
        return self.text[:30]



