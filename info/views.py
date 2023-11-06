from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from info.form import InfoCollectionForm, CollectionRecordForm
from info.models import InfoCollection, CollectionRecord


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
    # template_name = 'relation/relation_create.html'
    form_class = InfoCollectionForm
    # fields = ('name', 'owner', 'start_year', 'number_records', 'collection_cost')
    # success_url = '/collections'

    def get_success_url(self):
        return reverse('collection-list')

    def form_valid(self, form):
        response = super().form_valid(form)

        selected_records = form.cleaned_data.get('records')

        if selected_records is not None:
            collection_record_objects = [
                CollectionRecord(collection=self.object, record=record)
                for record in selected_records
            ]

            CollectionRecord.objects.bulk_create(collection_record_objects)

        return response


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


class CollectionRecordListView(generic.ListView):
    model = CollectionRecord
    template_name = 'relation/relation_list.html'
    context_object_name = 'relations'
    # queryset = CollectionRecord.objects.all()
    # ordering = 'price'


class CollectionRecordCreateView(generic.CreateView):
    template_name = 'relation/relation_create.html'
    form_class = CollectionRecordForm
    context_object_name = 'records'
    # form_class = InfoCollectionForm

    def get_success_url(self):
        return reverse('relation-list')

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #
    #     selected_records = form.cleaned_data.get('records')
    #
    #     if selected_records is not None:
    #         collection_record_objects = [
    #             CollectionRecord(collection=self.object, record=record)
    #             for record in selected_records
    #         ]
    #
    #         CollectionRecord.objects.bulk_create(collection_record_objects)
    #
    #     return response

