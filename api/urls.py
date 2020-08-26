from django.urls import path
from . import views
urlpatterns = [
   path('getjobs/',views.getjobs),
   path('apply/',views.apply),
   path('getstatus/',views.getstatus),
   path('getapps/',views.getapps),
   path('addinteview/',views.addinteview),
   path('getinterview/',views.getinterview),
   path('feedupdate/',views.feedupdate),
   
   
   
]
