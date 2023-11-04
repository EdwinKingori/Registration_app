from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('', views.RegFormView.as_view(), name='reg_view'),
    path('reg_complete/', views.reg_complete, name='reg_complete')
]
