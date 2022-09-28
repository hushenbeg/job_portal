from django.shortcuts import render
from jobapp.models import HydJob
from jobapp.models import PuneJob
from jobapp.models import BangaloreJob
from jobapp.models import ChennaiJob

# Create your views here.

def job_view(request):
    jobs = HydJob.objects.all()

    hb_tech = {
        'name':'HBTECHNOLOGY',

    }
    return render(request, 'tempapp/index.html', hb_tech)

def login_view(request):
    user_info = {
        "username":"xxxxxxxx",
        "password":"xxxxxxxx"
    }
    return render(request, 'tempapp/login.html', user_info)

def hyd_jobs(request):
    jobs = HydJob.objects.all()
    return render(request, 'tempapp/hyd.html', {'jobs':jobs})

def pune_jobs(request):
    jobs = PuneJob.objects.all()
    return render(request, 'tempapp/pune.html', {'jobs':jobs})

def chennai_jobs(request):
    jobs = ChennaiJob.objects.all()
    return render(request, 'tempapp/chennai.html', {'jobs':jobs})

def bangolore_jobs(request):
    jobs = BangaloreJob.objects.all()
    return render(request, 'tempapp/bangalore.html', {'jobs':jobs})
