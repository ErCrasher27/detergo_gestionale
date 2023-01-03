from django.urls import path, include

from detergo_gestionale_app import views

urlpatterns = [
    path('latest-cliente/', views.LatestClientiList.as_view())
]
