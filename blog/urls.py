"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
#In Python regular expressions, the syntax for named regular-expression
# groups is (?P<name>pattern), where name is the name of the group and pattern is
# some pattern to match.
urlpatterns = [
    '',(r'^$','blogpost.views.index'),
    url(r'^blog/(?P<slug>[^\.]+).html','blogpost.views.view_post',name='view_blog_post'),
    url(r'^admin/',include(admin.site.urls)),
]
#name:passing extra aarguments to view functions
#include:chops off whatever part of the url matched uup to that point
#and sends the ramaining strring to the included URLconf for further processing
#that is to say,match the url on several stages
#meanwhile,it received the captured arguments

