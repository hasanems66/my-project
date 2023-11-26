from django.urls import path
from . import views



app_name='account'
urlpatterns = [
    # path('login', views.user_login, name='user_login'),
    path('login', views.UserLoginView.as_view(), name='user_login'),
    path('logout', views.UserLogoutView.as_view(), name='user_logout'),
    path('otplogin', views.UserOtpLoginView.as_view(), name='user_otplogin'),
    path('checkotp', views.CheckOtpView.as_view(), name='user_checkotp'),
    path('user/edit', views.UserEditeView.as_view(), name='user_edite'),
    path('add/address', views.AddAdressView.as_view(), name='add_address'),



]