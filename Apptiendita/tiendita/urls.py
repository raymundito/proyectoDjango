"""
URL configuration for tiendita project.

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
from django.urls import path
#importar views
from empleado import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,  name="home"),
    path('crear/', views.crear,  name="crear"),
    path('crearUsuario/', views.crearUsuario,  name="crearUsuario"),
    path('crearRol/', views.crearRol,  name="crearRol"),
    path('editar/<int:id>', views.editar,  name="editar"),
    path('editarUsuario/<int:id>', views.editarUsuario,  name="editarUsuario"),
    path('editarRol/<int:id>', views.editarRol,  name="editarRol"),
    path('layout/', views.layouts,  name="layouts"),
    path('eliminar/<int:id>/', views.eliminar,  name="eliminar"),
    path('eliminarUsuario/<int:id>/', views.eliminarUsuario,  name="eliminarUsuario"),
    path('eliminarRol/<int:id>/', views.eliminarRol,  name="eliminarRol"),
    path('empleadoindex/', views.empleadoindex,  name="empleadoindex"),
    path('usuarioindex/', views.usuarioindex,  name="usuarioindex"),
    path('rolindex/', views.rolindex,  name="rolindex"),

]
