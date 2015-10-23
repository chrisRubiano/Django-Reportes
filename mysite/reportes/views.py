from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Reparacion, Calibracion
from django.shortcuts import redirect
from .forms import ReparacionForm, CalibracionForm

def inicio(request):
    return render(request, 'reportes/base.html', {})

def new_report(request):
    if request.method == "POST":
        form = ReparacionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/', pk=Reparacion.pk)
    else:
        form = ReparacionForm()
    return render(request, 'reportes/new_report.html', {'form': form})

def new_calibration(request):
    if request.method == "POST":
        form = CalibracionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/', pk=Calibracion.pk)
    else:
        form = CalibracionForm()
    return render(request, 'reportes/new_calibration.html', {'form': form})    