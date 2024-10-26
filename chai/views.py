from django.shortcuts import render
from .models import chaivariety
# Create your views here.
def all_chai(request):
    chais = chaivariety.objects.all()
    return render(request, 'chai/all_chai.html',{'chais':chais})