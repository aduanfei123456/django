from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.view_post,{"slug":"asd"},name='index'),

]