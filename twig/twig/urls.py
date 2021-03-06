"""twig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

# from django.conf import settings
# from django.contrib.staticfiles import views
from django.conf import settings
from django.conf.urls.static import static

from twig_blog.views import *

urlpatterns = [
    url(r'^admin/',     admin.site.urls),
#    url(r'^$',          HomeView.as_view(template_name='base.html')),
    url(r'^$',          HomeView.as_view(template_name='index.html')),
    url(r'^home/',      HomeView.as_view(template_name='base.html'),name="home"),
    url(r'^home2/',     HomeView2.as_view(template_name='index.html'),name="home2"),
    url(r'^contact/',   ContactView.as_view(template_name='contact.html'),name="contact"),
    url(r'^about/',     AboutView.as_view(template_name='about.html'),name="about"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


