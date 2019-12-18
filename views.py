from django.shortcuts import render
from .forms import HomeForm
from .methods import methods

def home(request):
    return render(request,'analytics/home.html')

def get(request):
    research = HomeForm()
    return render(request,'analytics/home.html',{'Entreprise':research})

def post(request):
    form = HomeForm(request.post)
    if form.is_valid():
        text = form.clean_data['recuperer']
        id =  methods.searchdata(text)
        args = {'obtained':methods.getdata(id)}
    return render(request,'analytics/home.html',args)
    
