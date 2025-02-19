from django.urls import path
from .views  import *

urlpatterns = [
    path("",Studentlist),
    path("add/",post_Studentlist),
    path("update/<int:id>/",update_Studentlist),  
    path("delete/<int:id>/",delete_Studentlist),
   


]