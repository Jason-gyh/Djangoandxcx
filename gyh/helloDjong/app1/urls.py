from django.urls import path,include
from app1 import views
urlpatterns = [
    path('sh/', views.show_aa),
    path('',views.show_a),
    path('show/<int:article_id>',views.get_d),
]