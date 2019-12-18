from .models import Actionmenee, Ministeres, Benificiares

class methods():
    def searchdata (name=''):
        obj = Benificiares.objects.filter(beneficiaire = name).first()
        id = obj.action_id
        return id
        
    def getdata (id = searchdata()):
        obj1 = Actionmenee.objects.filter(action_id = id)
        str1 = obj1.action
        str2 = obj1.action_autre
        obj2 = Ministeres.objects.filter(action_id = id)
        str3 = obj2.responsable_public
        str4 = obj2.departement_ministeriel
        return str1 + str2 + str3 + str4
