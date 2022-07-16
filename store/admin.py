from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UsersAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Customer, UsersAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)