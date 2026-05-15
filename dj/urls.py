from django.urls import path
from .views import home, about_us, contact_page      # we can either use * to define all functions that we create in views.py 
                                        #or simply we can write each functions name

urlpatterns = [
    path('home', home),
    path('about', about_us),
    path('contactpage', contact_page)
]
