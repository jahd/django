from django.db import models
class Actionmenee(models.Model):
    action = models.CharField(null = True,max_length = 144, verbose_name = 'action')
    action_id = models.IntegerField(primary_key = True , default = 0, verbose_name = 'action_id')
    action_autre = models.CharField(null = True, max_length = 144, verbose_name = 'action_autre')

class Ministeres(models.Model):
    action_id = models.ForeignKey(Actionmenee,on_delete=models.CASCADE, default = 0, verbose_name = 'action_id')
    responsable_public = models.CharField(null = True, max_length = 150, verbose_name = 'responsable_public')
    departement_ministeriel = models.CharField(max_length = 150, verbose_name = 'departement_ministriel')

class Benificiares(models.Model):   
    beneficiaire = models.CharField(max_length = 155, null = True, verbose_name = 'beneficiaire')
    action_id = models.ForeignKey(Actionmenee,on_delete=models.CASCADE, default = 0, verbose_name = 'action_id')
    en_propre = models.BooleanField(null = True, blank = True, verbose_name = 'en_propre')

class GeneralInformation(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=256, blank=True)
    zipcode = models.CharField(max_length=256, blank=True)
    last_activity = models.DateTimeField(blank=True, null=True)
    first_activity = models.DateTimeField(blank=True, null=True)
    organizations = models.BooleanField(default=False)
    third_parties = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    nif = models.CharField(max_length=256, unique=True)
    activities = models.BooleanField(default=False)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    website = models.URLField(blank=True)
    hatvp_name = models.CharField(max_length=256)
    country = models.CharField(max_length=32)
    acronym = models.CharField(max_length=32)
    nif_type = models.CharField(max_length=8)
    town = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
