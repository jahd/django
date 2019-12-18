import csv
from .models import Actionmenee, Benificiares, Ministeres


def import_csv():
    source1 = "HATVP/Database/10_actions_menees.csv"
        
    with open(source1, 'r') as csv_file:
        
        csv_reader = csv.reader(csv_file)
            
        for line in csv_reader:
            action = Actionmenee.create()
            action.action = line[0]
            action.action_id = line[1]
            action.action_autre = line[2]
            action.save()
            
    source2 = "HATVP/Database/13_ministeres_aai_api.csv"
    
    with open(source2,'r') as csv_file:
        
        csv_reader = csv.reader(csv_file)
        
        for line in csv_reader:
            ministre = Ministeres.create()
            ministre.action_id = line[0]
            ministre.responsable_public = line[1]
            ministre.departement_ministeriel = line[2]
            ministre.save()
            
    source3 = "HATVP/Database/11_beneficiaires.csv"
    
    with open(source3,'r') as csv_file:
        
        csv_reader = csv.reader(csv_file)
        
        for line in csv_reader:
            beneficiaire = Benificiares.create()
            beneficiaire.beneficiaire = line[0]
            beneficiaire.action_id = line[1]
            beneficiaire.en_propre = line[2]
            beneficiaire.save()
