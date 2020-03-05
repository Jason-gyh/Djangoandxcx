from django.urls import path,include
from apptupian import views
urlpatterns = [
    path('image/', views.image),
    path('image1/', views.ImageView.as_view()),
    path('imagetext/', views.ImageText.as_view()),
    path('CookeieTest/',views.CookeieTest.as_view()),
    path('CookeieTest2/',views.CookeieTest2.as_view()),
    path('authorize/',views.authorize.as_view())
]