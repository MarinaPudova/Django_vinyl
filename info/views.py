from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def site_description(request):
    return render(request, 'description.html')


def site_info_about(request):
    return render(request, 'contacts.html')


def read_collections(request):
    return render(request, 'collections.html')