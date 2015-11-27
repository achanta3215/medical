from django.contrib import admin
from .models import Customer,Bill,Medicine,Cart,Staff

admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(Medicine)
# admin.site.register(Cart)
admin.site.register(Staff)
