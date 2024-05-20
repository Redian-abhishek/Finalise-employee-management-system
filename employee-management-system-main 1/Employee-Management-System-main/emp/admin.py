from django.contrib import admin
from .models import Emp

class EmpAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'name', 'phone', 'address', 'working', 'department')
    search_fields = ('emp_id', 'name', 'phone', 'address', 'department')
    list_filter = ('working', 'department')
    list_per_page = 20

admin.site.register(Emp, EmpAdmin)
