from django.db import models

class Benificiaires(models.Model):
    __source__= "/HATV/Database/11_benificiaires.csv"
    
    enterprise_name = models.CharField(max_length = 50, verbose_name='beneficiaire_action_menee')
    action_representant_interet_id = models.IntegerField(verbose_name='action_representation_interet_id')
    action_propre = models.IntegerField(verbose_name='action_menee_en_propre')

class Ministere(models.Model):
    __source__= "/HATV/Database/13_ministeres_aai_api.csv"
    
    action_representant_interet_id = models.IntegerField(verbose_name='action_representation_interet_id') 
    responsable_public = models.CharField(max_length = 100, verbose_name='responsable_public')
    departement_ministeriel = models.CharField(max_length = 100, verbose_name='departement_ministriel')
    responsable_public_ou_dpt_ministeriel_autre = models.CharField(max_length = 100, verbose_name='responsable_public_ou_dpt_ministeriel_autre')
    
class action(models.Model):
    __source__="/HATV/Database/10_actions_menees.csv"
    
    action_menee = models.TextField(verbose_name = 'action_menee')
    action_representation_interet_id = models.IntegerField(verbose_name = 'action_representation_interet_id')
    action_menee_autre = models.TextField(verbose_name = 'action_menee_autre')
    

                    
class test():

class search():
    id = 1
    
