from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from info.models import InfoCollection
from record.models import Record
from rest.serializers import RecordSerializer, InfoCollectionSerializer


class RecordListCreateView(APIView):
    def get(self, request):
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response({'records': serializer.data})

    def post(self, request):
        records = request.data.get('records')
        serializer = RecordSerializer(data=records)
        if serializer.is_valid(raise_exception=True):
            new_record = serializer.save()
        list_serializer = RecordSerializer(new_record)
        return Response({'new_record': list_serializer.data})


class RecordRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        records = Record.objects.get(id=pk)
        serializer = RecordSerializer(records)
        return Response({'records': serializer.data})

    def put(self, request, pk):
        record = get_object_or_404(Record.objects.all(), pk=pk)
        data = request.data.get('records')
        serializer = RecordSerializer(data=data, instance=record, partial=True)
        if serializer.is_valid(raise_exception=True):
            new_record = serializer.save()
        list_serializer = RecordSerializer(new_record)
        return Response({'update_record': list_serializer.data})

    def delete(self, request, pk):
        record = get_object_or_404(Record.objects.all(), pk=pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InfoCollectionListCreateView(APIView):
    def get(self, request):
        records = InfoCollection.objects.filter(is_open_viewing=True)
        serializer = InfoCollectionSerializer(records, many=True)
        return Response({'collections': serializer.data})

    def post(self, request):
        records = request.data.get('collections')
        serializer = InfoCollectionSerializer(data=records)
        if serializer.is_valid(raise_exception=True):
            new_collection = serializer.save()
        list_serializer = InfoCollectionSerializer(new_collection)
        return Response({'new_collection': list_serializer.data})


class InfoCollectionRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        collections = InfoCollection.objects.get(id=pk)
        serializer = InfoCollectionSerializer(collections)
        return Response({'collections': serializer.data})

    def put(self, request, pk):
        collection = get_object_or_404(InfoCollection.objects.all(), pk=pk)
        data = request.data.get('collections')
        serializer = InfoCollectionSerializer(data=data, instance=collection, partial=True)
        if serializer.is_valid(raise_exception=True):
            new_collection = serializer.save()
        list_serializer = InfoCollectionSerializer(new_collection)
        return Response({'update_collection': list_serializer.data})

    def delete(self, request, pk):
        collection = get_object_or_404(InfoCollection.objects.all(), pk=pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
