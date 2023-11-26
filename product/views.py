from django.shortcuts import render,get_object_or_404
from .models import Product
from django.views.generic import DetailView


class ProductDetailView(DetailView):
    model = Product
    # template_name = 'product/product_detail.html'
    slug_field = 'slug'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # self.request.session['my_name'] = 'hasan'
    #     # print(self.request.session['my_name'])
    #     # del self.request.session['my_name']
    #
    #     print(self.request.session.get('my_name', "ali"))
    #     return context

