from django.contrib import admin
from .models import (
    UserProfile, Address, Leave, Payroll
)
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(Leave)
admin.site.register(Payroll)