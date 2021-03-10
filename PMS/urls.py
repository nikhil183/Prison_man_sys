"""PMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app1 import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name = "home"),
    path('admin_after_login/', views.admin_after_login , name = "admin_after_login") ,
    path('jailor_after_login/', views.jailor_after_login , name = "jailor_after_login") ,
    path('lawyer_after_login/', views.lawyer_after_login , name = "lawyer_after_login") ,
    path('logout/' , views.logout_user , name = "logout") ,
    path('login/' , views.login_user , name = "login") ,
    path('viewprisoner/' , views.viewprisoner , name = "viewprisoner") ,
    path('addprisoner/' , views.addprisoner , name = "addprisoner") ,
    path('addjailor/' , views.addjailor , name = "addjailor") ,
    path('viewjailor/' , views.viewjailor , name = "viewjailor") ,
    path('viewlawyer/' , views.viewlawyer , name = "viewlawyer") ,
    path('jailorinfo/' , views.jailorinfo , name = "jailorinfo") ,
    path('prisonerinfo/<id>' , views.prisonerinfo , name = "prisonerinfo") ,
    path('addlawyer/' , views.addlawyer , name = "addlawyer")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
