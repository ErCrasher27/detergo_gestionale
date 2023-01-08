from django.urls import path, include

from detergo_gestionale_app import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('items/', views.ItemList.as_view()),
    path('colors/', views.CustomerList.as_view()),
    path('carriedItems/', views.BroughtItemList.as_view()),
    
    path('itemsByCategory/<int:idCategory>/', views.ItemsListByCategory.as_view()),
    path('categoriesByMaxi/<str:maxi>/', views.CategoriesByMaxi.as_view())
]
