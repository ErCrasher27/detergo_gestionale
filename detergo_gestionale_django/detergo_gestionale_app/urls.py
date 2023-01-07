from django.urls import path, include

from detergo_gestionale_app import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('items/', views.ItemList.as_view()),
    path('colors/', views.CustomerList.as_view()),
    path('defects/', views.DefectList.as_view()),
    path('carriedItems/', views.BroughtItemList.as_view()),
]
