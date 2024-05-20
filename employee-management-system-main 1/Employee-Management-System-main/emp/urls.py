from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path('signup/', signup, name ='signup'),
    path('signin/', signin, name = 'signin'),
    path('search', search, name='search'),
    path('signout/', signout, name = 'logout'),
    path('chart/',chart,name='chart')
]
