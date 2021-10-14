from django.contrib import admin

# Register your models here.
from .models import Expense, Category, Payment
admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(Payment)
