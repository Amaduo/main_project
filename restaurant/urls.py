from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('view/', views.view, name='view'),
    # path('question/', views.question, name='question'),
    path('message/', views.message, name='message'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('view_data/', views.view_data, name='view_data'),
    path('reservation/', views.reservation, name='reservation'),
    path('delete/', views.reservation, name='delete'),
    path('orders/', views.order, name='orders'),
    path('pay/', views.pay, name='pay'),
    # path('form/', views.form, name='form'),

]