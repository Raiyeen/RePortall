"""
URL configuration for RePortall project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RePortall import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    # path('report/', views.report, name='report'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('review/', views.review, name='review'),
    path('savereport/', views.savereport, name='savereport'),
    path('after-login/', views.after_login_redirect, name='after_login'),
    path('update-review/<int:pk>/', views.update_review, name='update_review'),
    path('delete-review/<int:pk>/', views.delete_review, name='delete_review'),
    path('Update_review_admin/update/<int:pk>/', views.update_review_admin, name='update_review_admin'),
    path('review/delete/<int:pk>/', views.delete_review_admin, name='delete_review_admin'),


]
