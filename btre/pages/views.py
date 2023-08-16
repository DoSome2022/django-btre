from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Realtor

# Create your views here.
def index(request):
    return render(request,"pages/index.html")

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.filter(is_mvp=True).first()
    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor,
    }

    return render(request,"pages/about.html")