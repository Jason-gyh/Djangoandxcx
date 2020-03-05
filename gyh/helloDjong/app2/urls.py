from django.urls import path,include
from app2 import views
urlpatterns = [
    path('juhe/',views.hellojuhe),
    path('apps',views.apps),
]