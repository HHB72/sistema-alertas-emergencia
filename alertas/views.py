from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm
from .models import GuiaPrimerosAuxilios, ContactoEmergencia, Incidente

def index(request):
    return render(request, 'index.html')

def sos(request):
    return render(request, 'sos.html')

def primeros_auxilios(request):
    guias = GuiaPrimerosAuxilios.objects.all()
    return render(request, 'primeros_auxilios.html', {'guias': guias})

def contactos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        if nombre and telefono:
            ContactoEmergencia.objects.create(nombre=nombre, telefono=telefono)
            return redirect('contactos')
    
    lista_contactos = ContactoEmergencia.objects.all()
    return render(request, 'contactos.html', {'contactos': lista_contactos})

def incidentes(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        afectados = request.POST.get('afectados')
        descripcion = request.POST.get('descripcion')
        if tipo and afectados:
            Incidente.objects.create(
                tipo=tipo,
                afectados=afectados,
                descripcion=descripcion
            )
            return redirect('incidentes')

    lista_incidentes = Incidente.objects.all().order_by('-fecha_creacion')
    return render(request, 'incidentes.html', {'incidentes': lista_incidentes})

def hospitales(request):
    return render(request, 'hospitales.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Encripta la clave sin validar longitud ni complejidad
            user.save()
            login(request, user)  # Inicia sesión automáticamente tras el registro
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})