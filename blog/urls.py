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
from blogpost import views as blogpostViews
from django.contrib.auth.models import User
from rest_framework import routers
from blogpost.api import BlogpostSet
apiRouter=routers.DefaultRouter()
apiRouter.register(r'blogpost',BlogpostSet)
urlpatterns = [
    url(r'^api_auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api/',include(apiRouter.urls)),
    url(r'^$',blogpostViews.index),
    url(r'^pages/',include('django.contrib.flatpages.urls')),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^blog/(?P<slug>[^\.]+).html', blogpostViews.view_post, name='view_blog_post'),
    url(r'^comments/',include('django_comments.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#name:passing extra aarguments to view functions
#include:chops off whatever part of the url matched uup to that point
#and sends the ramaining strring to the included URLconf for further processing
#that is to say,match the url on several stages
#meanwhile,it received the captured arguments

