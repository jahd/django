from django.shortcuts import render
from .forms import HomeForm
from .models import Actionmenee, Ministeres, Benificiares

def home(request):
    return render(request,'analytics/home.html')

def get(request):
    research = HomeForm()
    return render(request,'analytics/home.html',{'Entreprise':research})

def post(request):
    form = HomeForm(request.post)
    if form.is_valid():
        text = form.clean_data['recuperer']
        id =  searchdata(text)
        args = {'obtained':getdata(id)}
    return render(request,'analytics/home.html',args)

def searchdata (name=''):
    obj = Benificiares.objects.filter(beneficiaire = name).first()
    id = obj.action_id
    return id
    
def getdata (id):
    obj1 = Actionmenee.objects.filter(action_id = id)
    str1 = obj1.action
    str2 = obj1.action_autre
    obj2 = Ministeres.objects.filter(action_id = id)
    str3 = obj2.responsable_public
    str4 = obj2.departement_ministeriel
    return str1 + str2 + str3 + str4
   
