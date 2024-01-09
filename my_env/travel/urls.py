"""
URL configuration for travel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from travel_love.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from travel_love import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',travel, name="travel"),
    path('travel/',travel, name="travel" ),

    path('delete_travel/<id>/',views.delete_travel, name="delete_travel"),
    path('update_travel/<id>/',views.update_travel, name="update_travel"),

    path('login/',login_page, name="login_page" ),
    path('register/',register, name="register" ),
    path('logout/',logout_page, name="logout_page")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
