from django.http import HttpResponse
from django.template import loader
from django.db.models import Q

from .models import Actionmenee, Ministeres, Benificiares

    
def index(request):
    Beneficiaires = Benificiares.objects.order_by('id')[0:3]
    template = loader.get_template('analytics/index.html')
    context = {
            'Beneficiaires':Beneficiaires
            }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    Beneficiaires = get_object_or_404(Benificiares, pk= id) 
    dep =', '.join( str(x) for x in Ministeres.objects.filter(id = id))
    res = ', '.join(str(x.responsable_public) for x in Ministeres.objects.filter(id = id))
    act = ', '.join(str(x.action) for x in Actionmenee.objects.filter(id = id))
    pr = ', '.join(str(x.en_propre) for x in Benificiares.objects.filter(id = id))
    return render(request, 'analytics/detail.html', {'Bene': Beneficiaires, 'obj':dep, 'res':res, 'act':act, 'pr':pr})
  
def search (request):
    template = 'analytics/detail.html'
    
    query = request.GET.get('q')
    
    results = Benificiares.objects.filter(Q(beneficiaire__icontains=query))
    
    id = results[0].id
    
    dep =', '.join( str(x) for x in Ministeres.objects.filter(id = id))
    res = ', '.join(str(x.responsable_public) for x in Ministeres.objects.filter(id = id))
    act = ', '.join(str(x.action) for x in Actionmenee.objects.filter(id = id))
    pr = ', '.join(str(x.en_propre) for x in Benificiares.objects.filter(id = id))
    
    context = {
            'Bene':results[0],'obj':dep, 'res':res, 'act':act, 'pr':pr
            }
    return render(request, template, context)

