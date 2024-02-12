from django.contrib import admin
from django.urls import path,include
from .views import * # Use relative import for views
 
urlpatterns = [
    path("home/",Emp_home),
    path("add-Emp/",add_emp), 
      path("delete-Emp/<int:emp_id>",delete_emp),
      path("update-Emp/<int:emp_id>",update_emp),
       path("do-update-Emp/<int:emp_id>",do_update_emp),
       
]

    
