from django.urls import path
from . import views
urlpatterns = [
    path('', views.index ),
    path('request/', views.request ),
    path('signup/', views.signup ),
    path('europ/', views.europ ),
    path('liste/', views.liste ),

]
