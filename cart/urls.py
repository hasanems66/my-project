from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('detail', views.CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>', views.CartAddView.as_view(), name='cart_add'),
    path('delete/<str:id>', views.CartDeleteView.as_view(), name='cart_delete'),
    path('order/add', views.OrderCreation.as_view(), name='order_creation'),
    path('order/detail/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('applydicount/<int:pk>', views.ApplayDiscountView.as_view(), name='apply_discount'),
    path('sendrequest/<int:pk>', views.SendRequestView.as_view(), name='send_request'),
    path('verify/', views.VerifyView.as_view(), name='verify_request'),
]
