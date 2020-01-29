from django.db import models

class Action(models.Model):

    id = models.IntegerField(primary_key=True, verbose_name="action_representation_interet_id")
    
    def __str__(self):
        return self.id

class Actionmenee(models.Model):

    action = models.TextField(verbose_name="action_menee")
    id = models.IntegerField(primary_key=True, verbose_name="action_representation_interet_id")
    more = models.TextField(verbose_name="action_menee_autre")
    
    def __str__(self):
        return self.action


class Ministeres(models.Model):
    
    id = models.IntegerField(primary_key=True, verbose_name="action_representation_interet_id")
    responsable_public = models.CharField(null = True, max_length = 150, verbose_name = 'responsable_public')
    departement_ministeriel = models.CharField(max_length = 150, verbose_name = 'departement_ministeriel')
    
    def __str__(self):
        return self.departement_ministeriel


class Benificiares(models.Model):
    
    beneficiaire = models.CharField(max_length = 155, null = True, verbose_name = 'beneficiaire_action_menee')
    id = models.IntegerField(primary_key=True, verbose_name="action_representation_interet_id")
    en_propre = models.BooleanField(null = True, blank = True, verbose_name = 'action_menee_en_propre')

    def __str__(self):
        return self.beneficiaire

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
