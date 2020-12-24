from django.contrib import admin
from django.urls import path, include
from lists import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/first-list/', views.view_list, name='view_list'),
    path('admin/', admin.site.urls),
]
