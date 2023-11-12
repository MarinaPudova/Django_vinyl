from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from info.models import InfoCollection, CollectionRecord
from record.models import Record
from rest.serializers import RecordListSerializer, RecordCreateSerializer, RecordRetrieveSerializer, \
    RecordUpdateSerializer, InfoCollectionListSerializer, InfoCollectionCreateSerializer, \
    InfoCollectionRetrieveSerializer, InfoCollectionUpdateSerializer, InfoCollectionDestroySerializer


# from rest.serializers import RecordSerializer, InfoCollectionSerializer


# class RecordListCreateView(APIView):
#     def get(self, request):
#         records = Record.objects.all()
#         serializer = RecordSerializer(records, many=True)
#         return Response({'records': serializer.data})
#
#     def post(self, request):
#         records = request.data.get('records')
#         serializer = RecordSerializer(data=records)
#         if serializer.is_valid(raise_exception=True):
#             new_record = serializer.save()
#         list_serializer = RecordSerializer(new_record)
#         return Response({'new_record': list_serializer.data})
#
#
# class RecordRetrieveUpdateDeleteView(APIView):
#     def get(self, request, pk):
#         records = Record.objects.get(id=pk)
#         serializer = RecordSerializer(records)
#         return Response({'records': serializer.data})
#
#     def put(self, request, pk):
#         record = get_object_or_404(Record.objects.all(), pk=pk)
#         data = request.data.get('records')
#         serializer = RecordSerializer(data=data, instance=record, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             new_record = serializer.save()
#         list_serializer = RecordSerializer(new_record)
#         return Response({'update_record': list_serializer.data})
#
#     def delete(self, request, pk):
#         record = get_object_or_404(Record.objects.all(), pk=pk)
#         record.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # class InfoCollectionListCreateView(APIView):
#     def get(self, request):
#         records = InfoCollection.objects.filter(is_open_viewing=True)
#         serializer = InfoCollectionSerializer(records, many=True)
#         return Response({'collections': serializer.data})
#
#     def post(self, request):
#         records = request.data.get('collections')
#         serializer = InfoCollectionSerializer(data=records)
#         if serializer.is_valid(raise_exception=True):
#             new_collection = serializer.save()
#         list_serializer = InfoCollectionSerializer(new_collection)
#         return Response({'new_collection': list_serializer.data})
#
#
# class InfoCollectionRetrieveUpdateDeleteView(APIView):
#     def get(self, request, pk):
#         collections = InfoCollection.objects.get(id=pk)
#         serializer = InfoCollectionSerializer(collections)
#         return Response({'collections': serializer.data})
#
#     def put(self, request, pk):
#         collection = get_object_or_404(InfoCollection.objects.all(), pk=pk)
#         data = request.data.get('collections')
#         serializer = InfoCollectionSerializer(data=data, instance=collection, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             new_collection = serializer.save()
#         list_serializer = InfoCollectionSerializer(new_collection)
#         return Response({'update_collection': list_serializer.data})
#
#     def delete(self, request, pk):
#         collection = get_object_or_404(InfoCollection.objects.all(), pk=pk)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # class RecordView(generics.ListCreateAPIView): #  тогда можем не расписывать методы отдельно ниже
# class RecordView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Record.objects.all()
#     serializer_class = RecordSerializer
#
#     def list(self, request, *args, **kwargs):
#         realise_year = request.query_params.get('realise_year')
#         sorting = request.query_params.get('sorting')
#         if realise_year:
#             self.queryset = self.queryset.filter(realise_year__gte=realise_year)  # фильтрация больше или равно
#         if sorting:
#             self.queryset = self.queryset.order_by(sorting)
#         return super().list(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SingleRecordView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Record.objects.all()
#     serializer_class = RecordSerializer

# class RecordViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Record.objects.all()
#         serializer = RecordSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Record.objects.all()
#         record = get_object_or_404(queryset, pk=pk)
#         serializer = RecordSerializer(record)
#         return Response(serializer.data)

class RecordViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Information about records
    """
    queryset = Record.objects.all()
    serializer_class = RecordListSerializer
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

    # @action(detail=False, method=['get'], url_path='recent_books')
    # def recent_books(self, request):
    #     recent_books = Book.objects.filter(year__gte=2020)
    #     serializer = BooksSerializer(recent_books, many=True)
    #     return Response(serializer.data)


class InfoCollectionViewSet(viewsets.ModelViewSet):
    """
     Information about collections
    """
    queryset = InfoCollection.objects.all()
    serializer_class = InfoCollectionListSerializer
    serializer_classes = {
        'list': InfoCollectionListSerializer,
        'create': InfoCollectionCreateSerializer,
        'retrieve': InfoCollectionRetrieveSerializer,
        'update': InfoCollectionUpdateSerializer,
        'delete': InfoCollectionDestroySerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
