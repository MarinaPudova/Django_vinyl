from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from info.form import InfoCollectionForm
from info.models import InfoCollection

# Create your views here.


def site_description(request):
    return render(request, 'description.html')


def site_info_about(request):
    return render(request, 'contacts.html')


def read_collections(request):
    return render(request, 'collections.html')


class CollectionListView(generic.ListView):
    model = InfoCollection
    template_name = 'info_collection/collection_list.html'
    context_object_name = 'collections'
    # queryset = InfoCollection.objects.filter(is_deleted=False)
    # ordering = 'price'


class CollectionDetailView(generic.DetailView):
    model = InfoCollection
    template_name = 'info_collection/collection_detail.html'
    context_object_name = 'collection'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['collections'] = InfoCollection.objects.filter(is_deleted=False)
    #     return context


class CollectionCreateView(generic.CreateView):
    # model = InfoCollection
    template_name = 'info_collection/collection_create.html'
    form_class = InfoCollectionForm
    # fields = ('name', 'owner', 'start_year', 'number_records', 'collection_cost')
    # success_url = '/collections'

    def get_success_url(self):
        return reverse('collection-list')


class CollectionUpdateView(generic.UpdateView):
    model = InfoCollection
    template_name = 'info_collection/collection_update.html'
    form_class = InfoCollectionForm

    def get_success_url(self):
        return reverse('collection-list')


class CollectionDeleteView(generic.DeleteView):
    model = InfoCollection
    template_name = 'info_collection/collection_delete.html'

    def get_success_url(self):
        return reverse('collection-list')
