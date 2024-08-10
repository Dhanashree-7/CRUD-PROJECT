from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('add/',views.addproduct),
    path('all/',views.allproduct),
    path('saveproduct',views.saveproduct),
    path('delete/<rid>',views.deleteproduct),
    path('edit/<rid>',views.editproduct),
]