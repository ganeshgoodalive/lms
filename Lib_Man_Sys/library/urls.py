from django.urls import path
from library import views

urlpatterns = [
    path('home',views.home),
    #path('modelform',views.modelform),
    path('form',views.form),
    path('update/<int:tid>',views.update),
    path('to_archive/<int:tid>',views.to_archive),
    path('archive_data',views.archive_data),
    




]
