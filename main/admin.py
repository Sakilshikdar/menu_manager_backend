from django.contrib import admin
from .models import AdminCustomer, Menu, Review
# Register your models here.
admin.site.register(AdminCustomer)
admin.site.register(Menu)
admin.site.register(Review)
