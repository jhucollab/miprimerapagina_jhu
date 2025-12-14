from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import RegistroForm

def login_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Has iniciado sesión correctamente.")
            return redirect("inicio")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "usuarios/login.html")
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
def logout_usuario(request):
    logout(request)
    return redirect("inicio")
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado con éxito. Ahora inicia sesión.")
            return redirect("login")
    else:
        form = RegistroForm()

    return render(request, "usuarios/registro.html", {"form": form})
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import CV
from .forms import CVForm

class VerCV(LoginRequiredMixin, DetailView):
    model = CV
    template_name = "usuarios/cv_detalle.html"

    def get_object(self, queryset=None):
        return CV.objects.filter(usuario=self.request.user).first()

class CrearCV(LoginRequiredMixin, CreateView):
    model = CV
    form_class = CVForm
    template_name = "usuarios/cv_form.html"

    def dispatch(self, request, *args, **kwargs):
        existente = CV.objects.filter(usuario=request.user).first()
        if existente:
            return redirect("editar_cv", pk=existente.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("ver_cv")

class EditarCV(LoginRequiredMixin, UpdateView):
    model = CV
    form_class = CVForm
    template_name = "usuarios/cv_form.html"
    def get_queryset(self):
        return CV.objects.filter(usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy("ver_cv")

class BorrarCV(LoginRequiredMixin, DeleteView):
    model = CV
    template_name = "usuarios/cv_confirm_delete.html"
    success_url = reverse_lazy("ver_cv")

    def get_queryset(self):
        return CV.objects.filter(usuario=self.request.user)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class PagSecreta(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/pag_secreta.html'


# Create your views here.
