"""Lib_Man_Sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('form',views.form),
    path('archive_data',views.archive_data),
    path('library/',include('library.urls')),
    path('update/<int:tid>',views.update),
    path('to_archive/<int:tid>',views.to_archive),
    path('restore/<int:tid>',views.restore),
    path('delete/<int:tid>',views.delete),
    path('sort_by_price',views.sort_by_price),
    path('sort_by_price_rev',views.sort_by_price_rev),
    path('sort_by_authorname',views.sort_by_authorname),
    path('sort_by_authorname_rev',views.sort_by_authorname_rev),
    path('real_myth',views.real_myth),
    path('sort_by_bookname',views.sort_by_bookname),
    path('sort_by_bookname_rev',views.sort_by_bookname_rev),
    path('sort_by_type',views.sort_by_type),
    path('sort_by_publisher',views.sort_by_publisher),
    path('sort_by_published_on',views.sort_by_published_on),
    path('non_fiction',views.non_fiction),
    path('edited',views.edited),
    path('reference',views.reference),
    path('fiction',views.fiction),
    #path('accounts/',include('django.contrib.auth.urls')),

    #path('welcome',views.welcome),
    path('data',views.data),

    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('header',views.header)



]
