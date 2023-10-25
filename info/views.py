from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from info.models import InfoCollection


# Create your views here.


def site_description(request):
    return render(request, 'description.html')


def site_info_about(request):
    return render(request, 'contacts.html')


# def read_collections(request):
#     return render(request, 'collections.html')


class CollectionView(View):
    def get(self, request, id=None):
        collections = InfoCollection.objects.all()
        if id:
            collection = InfoCollection.objects.filter(id=id).first()
            return render(request, 'collection.html', context={'collection': collection})
        return render(request, 'collections.html', context={'collections': collections})
