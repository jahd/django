from django.db import models

class Actionmenee(models.Model):
    __source__ = "HATVP/Database/10_actions_menees.csv"
    
    action_menee = models.TextField()
    action_representation_interet_id = models.IntegerField(primary_key = True, verbose_name="action_representation_interet_id")
    action_menee_autre = models.TextField()
