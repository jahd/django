from django.db import models
from .action_menée import Actionmenee

class Ministeres(models.Model):
    __source__ = "HATVP/Database/13_ministeres_aai_api.csv"
    
    action_representation_interet_id = models.ForeignKey(Actionmenee, verbose_name="action_representation_interet_id",on_delete=models.CASCADE)
    responsable_public = models.CharField(max_length = 150, verbose_name="responsable_public")
    departement_ministeriel = models.CharField(max_length = 150, verbose_name="departement_ministeriel")
    #responsable_public_ou_dpt_ministeriel_autre
