from django.urls import path
from . import views


urlpatterns = [
    path("", views.test, name="index"),
    path("gererId",views.gestionId,name="gestion_des_ID"),
    path("gestionIdRequete",views.gestionIdRequete,name= "fonctionEnvoi_ID"),
    path("statistiques",views.statistiques, name= "statistiques"),
    path("statistiques/suppressionUser/<int:id>/", views.supprUser, name= "supprimer_user")
]