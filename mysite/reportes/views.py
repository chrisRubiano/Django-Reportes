from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Reparacion, Calibracion
from django.shortcuts import redirect
from .forms import ReparacionForm, CalibracionForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

def inicio(request):
    return render(request, 'reportes/index.html', {})

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

def report_list(request):
    reparaciones = Reparacion.objects.filter(fecha__lte=timezone.now()).order_by('-fecha')
    return render(request, 'reportes/report_list.html', {'reparaciones': reparaciones})

def report_detail(request, pk):
    reparacion = get_object_or_404(Reparacion, pk=pk)
    return render(request, 'reportes/report_detail.html', {'reparacion': reparacion})

def calibration_list(request):
    calibraciones = Calibracion.objects.filter(fecha__lte=timezone.now()).order_by('-fecha')
    return render(request, 'reportes/calibration_list.html', {'calibraciones': calibraciones})

def calibration_detail(request, pk):
    calibracion = get_object_or_404(Calibracion, pk=pk)
    return render(request, 'reportes/calibration_detail.html', {'calibracion': calibracion})

#esta vista es para las calibraciones pendientes/es codigo copiado de calibration_list
def calibration_pending(request):
    calibraciones = Calibracion.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'reportes/calibration_pending.html', {'calibraciones': calibraciones})


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Usuario/Contrasena incorrectos")
    else:
        return render_to_response('reportes/login.html', {}, context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')