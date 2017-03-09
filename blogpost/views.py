from django.shortcuts import render,render_to_response,get_object_or_404
from blogpost.models import Blogpost
from  blogpost.api import BlogpostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return render_to_response('index.html',{'posts':Blogpost.objects.all()[:5]})
# Create your views here.
def view_post(request, slug):
    return render_to_response('blogpost_detail.html', {
        'post': get_object_or_404(Blogpost, slug=slug)
    })





