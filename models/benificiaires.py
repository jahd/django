from django.db import models
from .action_menée import Actionmenee

class Benificiares(models.Model):
    __source__="HATVP/Database/11_beneficiaires.csv"
    
    beneficiaire_action_menee = models.CharField(max_length = 155, verbose_name="beneficiaire_action_menee")
    action_representation_interet_id = models.ForeignKey(Actionmenee, verbose_name="action_representation_interet_id",on_delete=models.CASCADE)
    action_menee_en_propre = models.BooleanField(verbose_name="action_menee_en_propre")