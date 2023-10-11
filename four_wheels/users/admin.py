from django.contrib import admin

from .models import BannedUser, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'mobile_phone')
    list_filter = ('email',)
    empty_value_display = '-empty-'


@admin.register(BannedUser)
class BannedUserAdmin(admin.ModelAdmin):
    list_display = ('user_banned', 'is_locked')
