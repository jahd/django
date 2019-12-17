from django.db import models


class Actionmenee(models.Model):
    __source__ = "HATVP/Database/10_actions_menees.csv"
    
    action_menee = models.TextField()
    action_representation_interet_id = models.IntegerField(primary_key = True, verbose_name="action_representation_interet_id")
    action_menee_autre = models.TextField()

class Ministeres(models.Model):
    __source__ = "HATVP/Database/13_ministeres_aai_api.csv"
    
    action_representation_interet_id = models.ForeignKey(Actionmenee, verbose_name="action_representation_interet_id",on_delete=models.CASCADE)
    responsable_public = models.CharField(max_length = 150, verbose_name="responsable_public")
    departement_ministeriel = models.CharField(max_length = 150, verbose_name="departement_ministeriel")

class Benificiares(models.Model):
    __source__="HATVP/Database/11_beneficiaires.csv"
    
    beneficiaire_action_menee = models.CharField(max_length = 155, verbose_name="beneficiaire_action_menee")
    action_representation_interet_id = models.ForeignKey(Actionmenee, verbose_name="action_representation_interet_id",on_delete=models.CASCADE)
    action_menee_en_propre = models.BooleanField(verbose_name="action_menee_en_propre")
    
class GeneralInformation(models.Model):
    __source__ = "hatvp/Database/1_informations_generales.csv"

    id = models.IntegerField(primary_key=True, verbose_name="representants_id")
    address = models.CharField(max_length=256, verbose_name="adresse", blank=True)
    zipcode = models.CharField(max_length=256, verbose_name="code_postal", blank=True)
    last_activity = models.DateTimeField(verbose_name="derniere_publication_activite", blank=True, null=True)
    first_activity = models.DateTimeField(verbose_name="date_premiere_publication", blank=True, null=True)
    organizations = models.BooleanField(verbose_name="declaration_organisation_appartenance", default=False)
    third_parties = models.BooleanField(verbose_name="declaration_tiers", default=False)
    name = models.CharField(max_length=256, verbose_name="denomination")
    nif = models.CharField(max_length=256, unique=True, verbose_name="identifiant_national")
    activities = models.BooleanField(verbose_name="activites_publiees", default=False)
    facebook = models.URLField(verbose_name="page_facebook", blank=True)
    linkedin = models.URLField(verbose_name="page_linkedin", blank=True)
    twitter = models.URLField(verbose_name="page_twitter", blank=True)
    website = models.URLField(verbose_name="site_web", blank=True)
    hatvp_name = models.CharField(max_length=256, verbose_name="nom_usage_HATVP")
    country = models.CharField(max_length=32, verbose_name="pays")
    acronym = models.CharField(max_length=32, verbose_name="sigle_HATVP")
    nif_type = models.CharField(max_length=8, verbose_name="type_identifiant_national")
    town = models.CharField(max_length=64, verbose_name="ville")
    category = models.CharField(max_length=64, verbose_name="label_categorie_organisation")
    