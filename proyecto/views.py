from django.shortcuts import render
from .models import Energia, Particula
#listado energia(mostrar)
def listado_energia(request):
    query = request.GET.get("q")
    if query:
        energias = Energia.objects.filter(tipo__icontains=query)
    else:
        energias = Energia.objects.all()
    return render(request, "listado_energia.html", {"energias": energias})
#listado particula
def listado_particulas(request):
    query = request.GET.get("q")
    if query:
        particulas = Particula.objects.filter(carga_electrica__icontains=query)
    else:
        particulas = Particula.objects.all()
    return render(request, "listado_particula.html", {"particulas": particulas})

# Create your views here.
from .forms import EnergiaForm, ParticulaForm
from django.shortcuts import render, redirect
#crear energia formulario
def crear_energia(request):
    if request.method == "POST":
        form = EnergiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listado_energia")
    else:
        form = EnergiaForm()

    return render(request, "crear_energia.html", {
        "form": form,
        "usuario_registrado": request.user.is_authenticated
    })
#crear particula formulario
def crear_particula(request):
    if request.method == "POST":
        form = ParticulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listado_particula")
    else:
        form = ParticulaForm()
    return render(request, "crear_particula.html", {"form": form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Energia, Particula
#editar
def editar_energia(request, id):
    energia = get_object_or_404(Energia, id=id)

    if request.method == "POST":
        form = EnergiaForm(request.POST, request.FILES, instance=energia)
        if form.is_valid():
            form.save()
            return redirect("listado_energia")
    else:
        form = EnergiaForm(instance=energia)

    return render(request, "editar_energia.html", {"form": form, "energia": energia})

def editar_particula(request, id):
    particula = get_object_or_404(Particula, id=id)
    if request.method == 'POST':
        particula.nombre = request.POST.get('nombre')
        particula.carga_electrica = request.POST.get('carga_electrica')
        particula.save()
        return redirect('listado_particula')
    return render(request, 'editar_particula.html', {'particula': particula})
#eliminar
def eliminar_energia(request, id):
    energia = get_object_or_404(Energia, id=id)
    if request.method == 'POST':
        energia.delete()
        return redirect('listado_energia')
    return render(request, 'eliminar_energia.html', {'energia': energia})
def eliminar_particula(request, id):
    particula = get_object_or_404(Particula, id=id)
    if request.method == 'POST':
        particula.delete()
        return redirect('listado_particula')
    return render(request, 'eliminar_particula.html', {'particula': particula})
def aboutme(request):
    return render(request, 'aboutme.html')
from django.views.generic import ListView
from django.contrib import messages
class EnergiaListView(ListView):
    model = Energia
    template_name = 'listado_energia.html'
    def get_queryset(self):
        q = self.request.GET.get('q')
        qs = super().get_queryset()
        if q:
            qs = qs.filter(nombre__incontains=q)
            if not qs:
                messages.info(self.request, 'no hay resultados')
                return qs
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required
def pag_secreta(request):
    return render(request, "usuarios/pag_secreta.html")

from django.shortcuts import render
def inicio(request):
    return render(request, "inicio.html")

          