from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, Contacto
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        
        Contacto.objects.create(
            nombre=nombre, 
            email=email, 
            mensaje=mensaje
        )
        
        messages.success(request, '¡Tu mensaje ha sido enviado! Me pondré en contacto pronto.')
        return redirect('home')

    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos})

def detalle_proyecto(request, pk):
    # Esta es la función que usa el get_object_or_404 corregido
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'detalle.html', {'proyecto': proyecto})