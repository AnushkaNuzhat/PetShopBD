
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('search/', views.search, name='search'),
    path('store/', views.store, name='store'),
    path('pet_details_categorised/<int:id>',
         views.Pet_Details_Categorised, name='pet_details_categorised'),
    path('pet_details/<int:id>', views.Pet_Details, name='pet_details')
    #     path('store/<slug:animalcategory_slug>/', views.store, name='animals_by_category'),
    #     path('store/<slug:animal_category_slug>/<slug:animal_slug>/', views.animal_detial, name='animal_detail'),
]
