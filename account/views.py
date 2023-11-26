from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views import View
from account.forms import UserLoginForm, UserRegisterForm, CheckOtpForm,UserChangeForm,AddressCreationForm
import ghasedakpack
from random import randint
from .models import User, Otp
from django.utils.crypto import get_random_string
from uuid import uuid4

sms = ghasedakpack.Ghasedak('f5e0deb95b0a29088a59c07ae31f9efe8b09669f7c4b2ab8c7c67c083b98bbbf')


# Create your views here.


# def user_login(request):
#     if request.method == 'POST':
#         username= request.POST.get('phone')
#         password = request.POST.get('password')
#         user=authenticate(request, phone=username, password=password)
#         # print(user.fullname)
#         if user is not None:
#             login(request, user)
#             return redirect('home:main')
#     return render(request, 'account/login.html', context={})

class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:main')
            else:
                form.add_error('phone', 'There is no user with this number')
        else:
            form.add_error('phone', 'The information entered is not correct')

        return render(request, 'account/login.html', context={'form': form})


class UserOtpLoginView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'account/otplogin.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # token = get_random_string(length=100)
            token = str(uuid4())
            randcode = randint(1000, 9999)
            # sms.verification({'receptor': cd['phone'], 'type': '1', 'template': 'randcode', 'param1': randcode})
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token)
            print(randcode)
            # return redirect(reverse('account:user_checkotp') + f'?phone={cd["phone"]}')
            return redirect(reverse('account:user_checkotp') + f'?token={token}')
        else:
            form.add_error('phone', 'invalid data')
        return render(request, 'account/otplogin.html', context={'form': form})


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'account/checkotplogin.html', context={'form': form})

    def post(self, request):
        # phone = request.GET.get('phone')   #کرفتن شماره تلفن ار طریق url که با ریورز ارسال میشه
        token = request.GET.get('token')   #کرفتن توکن ار طریق url که با ریورز ارسال میشه
        form = CheckOtpForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # if Otp.objects.filter(code=cd['code'], phone=phone).exists():
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                # user = User.objects.create_user(phone=otp.phone)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(request, user)
                otp.delete()
                return redirect('account:user_edite')
        else:
            form.add_error('phone', 'invalid data')
        return render(request, 'account/checkotplogin.html', context={'form': form})


class UserEditeView(View):
    def get(self,request):
        user = request.user
        form = UserChangeForm(instance=user)
        return render(request, 'account/user_edit.html', context={'form': form})

    def post(self,request):
        user = request.user
        form = UserChangeForm(data=request.POST, instance=user)
        if form.is_valid():
            # print(form.cleaned_data['phone'])
            form.save()
            return redirect('home:main')
        else:
            form = UserChangeForm(data=request.POST)

        return render(request, 'account/user_edit.html', {'form': form})



class AddAdressView(View):
    def get(self,request):
        form = AddressCreationForm()
        return render(request, 'account/add_address.html', context={'form': form})

    def post(self,request):
        form = AddressCreationForm(data=request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
        return render(request, 'account/add_address.html', context={'form': form})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home:main')
