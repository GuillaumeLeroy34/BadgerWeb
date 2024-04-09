from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("gererId",views.gestionId,name="gestion_des_ID"),
    path("gestionIdRequete",views.gestionIdRequete,name= "fonctionEnvoi_ID"),
    path("statistiques",views.statistiques, name= "statistiques"),
    path("statistiques/suppressionUser/<int:id>/", views.supprUser, name= "supprimer_user"),
    path("statistiques/changementAutorisation/<int:id>/", views.changementAutorisation, name="changement_autorisation")
]