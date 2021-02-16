from django.conf.urls import url
from django.urls import path
from account import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:form_id>/', views.show, name='show'),
]
