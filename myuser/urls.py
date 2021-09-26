from django.urls import path
from myuser import views

urlpatterns = [
    path('api_myuser/', views.snippet_list),
    path('api_myuser/<int:pk>/', views.snippet_detail),
    path('api_warehouse/', views.warehouse_list),
    path('api_warehouse/<int:pk>/', views.warehouse_detail),
    path('api_ware/', views.ware_list),
    path('api_ware/<int:pk>/', views.ware_detail),
    path('api_amount/', views.amount_list),
    path('api_order/', views.order_table_list),
    path('api_order/<int:pk>/', views.order_table_detial),
    path('api_statistic/ware_order/', views.ware_order_statistic)
]
