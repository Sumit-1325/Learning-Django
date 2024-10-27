from django.shortcuts import render
from .models import chaivariety
from django.shortcuts import get_object_or_404  
# Create your views here.
def all_chai(request):
    chais = chaivariety.objects.all()
    return render(request, 'chai/all_chai.html',{'chais':chais})

def chai_details(request,chai_id):
    chai = get_object_or_404(chaivariety, pk =chai_id)
    return render(request, "chai/chai_details.html",{'chai':chai})