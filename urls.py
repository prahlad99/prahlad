from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [

   path('',views.apiOverview,name="api-Overview"),
   path('favoritebook-list/',views.favoritebookList,name="favouritebook-list"),
   path('favoritebook-details/<str:pk>/', views.favoritebookDetails, name="favouritebook-details"),
   path('favoritebook-create/', views.favoritebookCreate, name="favouritebook-create"),
   path('favoritebook-update/<str:pk>/', views.favoritebookUpdate, name="favouritebook-update"),
   path('favoritebook-delete/<str:pk>/', views.favoritebookDelete, name="favouritebook-delete")]
