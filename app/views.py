from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Clinic
# Create your views here.
def home(request):
    clinics = Clinic.objects.all()
    return render(request, 'home.html', { 'clinics': clinics })

class ClinicCreate(CreateView):
    model = Clinic
    fields = '__all__'
    success_url = '/'

class ClinicDetail(DetailView):
    model = Clinic

class ClinicUpdate(UpdateView):
    model = Clinic
    fields = '__all__'
    success_url = '/'

class ClinicDelete(DeleteView):
    model = Clinic
    success_url = '/'