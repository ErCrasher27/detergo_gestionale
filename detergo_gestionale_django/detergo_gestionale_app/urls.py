from django.urls import path, include

from detergo_gestionale_app import views

urlpatterns = [
    path('clienti/', views.ClientiList.as_view())
]
