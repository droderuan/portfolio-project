from django.shortcuts import render

from .models import Job

# Create your views here.

def home(request):
    jobs = Job.objects.order_by('-id')   # O '-' na frente do atributo indica que a ordem deve ser decrescente
    return render(request, 'jobs/home.html', {'jobs': jobs})