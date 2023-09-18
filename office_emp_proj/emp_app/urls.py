from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  path('',views.index ,name='index'),
  path('addEmp',views.addEmp ,name='addEmp'),
  path('removeEmp',views.removeEmp ,name='removeEmp'),
  path('removeEmp/<int:emp_id>',views.removeEmp ,name='removeEmp'),
  path('allEmp',views.allEmp ,name='allEmp'),
  path('filterEmp',views.filterEmp ,name='filterEmp'),
]
