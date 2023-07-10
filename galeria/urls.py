"""
URL configuration for galeria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from photograph.views import UsuarioView, FotoListView, FotoDetailView, FotoAprovacaoView, ComentarioListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', UsuarioView.as_view(), name='usuario-list'),
    path('usuario/fotos/', FotoListView.as_view(), name='foto-list'),
    path('usuario/fotos/<int:pk>/', FotoDetailView.as_view(), name='foto-detail'),
    path('usuario/fotos/<int:pk>/aprovar/', FotoAprovacaoView.as_view(), name='foto-aprovar'),
    path('usuario/comentarios/', ComentarioListView.as_view(), name='comentario-list'),
]

