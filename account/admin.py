from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from account.models import User,Otp,Address




class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('phone','email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('اطلاعات شخصی', {'fields': ('fullname',)}),
        ('دسترسی ها', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fullname', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    list_editable = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ('phone', 'code')

@admin.register(Address)
class AdressAdmin(admin.ModelAdmin):
    list_display = ('user', '__str__')

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
