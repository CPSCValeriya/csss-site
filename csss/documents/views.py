from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

def index(request):
	print("constitution index")
	return render(request, 'documents/constitution.html')

def policies(request):
	print("policies index")
	return render(request, 'documents/policies.html')


def photo_gallery(request):
	print("photo_gallery not POST")
	return render(request, 'documents/photo_gallery.html')

def photos(request):
	print("photo gallery index")
	return render(request, 'documents/photo_gallery.html')