from rest_framework import mixins, viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as django_filters

from info.models import InfoCollection
from record.models import Record
from rest.filters import RecordFilter, InfoCollectionFilter
from rest.pagination import RecordPagination
from rest.permissions import AdminChangeRecordPermission
from rest.serializers import (
    RecordCreateSerializer,
    RecordListSerializer,
    RecordRetrieveSerializer,
    RecordUpdateSerializer,
    InfoCollectionCreateSerializer,
    InfoCollectionDestroySerializer,
    InfoCollectionListSerializer,
    InfoCollectionRetrieveSerializer,
    InfoCollectionUpdateSerializer,
)


class RecordViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    Information about records
    """
    queryset = Record.objects.all()
    serializer_class = RecordListSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = RecordFilter
    ordering = ('artist', '-realise_year')
    ordering_fields = ('id', 'name', 'artist', 'realise_year')
    search_fields = ('name', 'artist', 'realise_year')
    pagination_class = RecordPagination
    permission_classes = (AdminChangeRecordPermission, IsAuthenticated, )
    serializer_classes = {
        'list': RecordListSerializer,
        'create': RecordCreateSerializer,
        'retrieve': RecordRetrieveSerializer,
        'update': RecordUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @action(detail=True, methods=['get'], url_path='collections')
    def collections(self, request, pk=None):
        """
        return list of collections included our record
        :param request:
        :param pk:
        :return:
        """
        record = self.get_object()
        collections = InfoCollection.objects.filter(record=record.id)
        serializer = InfoCollectionListSerializer(collections, many=True)
        return Response(serializer.data)


class InfoCollectionViewSet(viewsets.ModelViewSet):
    """
     Information about collections
    """
    # queryset = InfoCollection.objects.all()  # без менеджеров
    queryset = InfoCollection.open_objects.all()
    serializer_class = InfoCollectionListSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = InfoCollectionFilter
    ordering = ('start_year', )
    ordering_fields = ('id', 'name', 'owner', 'start_year', )
    search_fields = ('name', 'owner', 'start_year', 'record__name', 'record_artist', 'record_realise_year')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_classes = {
        'list': InfoCollectionListSerializer,
        'create': InfoCollectionCreateSerializer,
        'retrieve': InfoCollectionRetrieveSerializer,
        'update': InfoCollectionUpdateSerializer,
        'delete': InfoCollectionDestroySerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
