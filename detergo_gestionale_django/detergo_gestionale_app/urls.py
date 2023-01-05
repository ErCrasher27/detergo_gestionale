from django.urls import path, include

from detergo_gestionale_app import views

urlpatterns = [
    path('clienti/', views.ClientiList.as_view()),
    path('ordini/', views.OrdiniList.as_view()),
    path('categorie/', views.CategorieList.as_view()),
    path('articoli/', views.ArticoliList.as_view()),
    path('colori/', views.ColoriList.as_view()),
    path('difetti/', views.DifettiList.as_view()),
    path('capiportati/', views.CapiPortatiList.as_view()),
]
