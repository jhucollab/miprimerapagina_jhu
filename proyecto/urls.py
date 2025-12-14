from django.urls import path, include
from . import views
from .views import aboutme, pag_secreta, EnergiaListView
from .views import inicio


urlpatterns = [
    path('energia/', views.listado_energia, name='listado_energia'),
    path('particula/', views.listado_particulas, name='listado_particula'),
    path('energia/nueva/', views.crear_energia, name='crear_energia'),
    path('particula/nueva/', views.crear_particula, name='crear_particula'),
    path('energia/<int:id>/editar/', views.editar_energia, name='editar_energia'),
    path('particula/<int:id>/eliminar', views.eliminar_energia, name='eliminar_energia'),
    path('particulas/<int:id>/editar/', views.editar_particula, name='editar_particula'),
    path('particulas/<int:id>/eliminar/', views.eliminar_particula, name='eliminar_particula'),
    path('aboutme/', aboutme, name='aboutme'),
    path("secreta/", pag_secreta, name="pag_secreta"),
    path('energia/', EnergiaListView.as_view(), name='listado_energia'),
    path("", inicio, name="inicio"),
    path("usuarios/", include("usuarios.urls")),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

