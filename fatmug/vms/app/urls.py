from django.urls import path,include
from app import views
urlpatterns = [
    path('', views.purchase_orders, name='home'),
    path('hp/<id>/',views.historicalperformance)
]