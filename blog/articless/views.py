from django.shortcuts import render
from django import template
from .models import Article
# Create your views here.
from django.http import HttpResponse
def archive(request):
        return render(request, 'templates/archive.html',{"posts": Article.objects.all()})
