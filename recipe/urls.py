from django.urls import path
from .views import recipe_list,create,update

urlpatterns = [
    path('recipe/',recipe_list),
    path('recipe/create/',create),
    path('recipe/<id>/',update),
]
