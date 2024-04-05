from django.urls import path
from . import views

app_name = "gestionId"
urlpatterns = [
    path("", views.test, name="index"),
    path("gererId",views.gestionId,name="gestion des ID"),
    path("gestionIdRequete",views.gestionIdRequete,name= "fonctionEnvoi ID"),
    path("statistiques",views.statistiques, name= "vue des stat")
]