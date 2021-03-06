from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


class SubjectAPI(APIView):
    def get(self, request, format=None):
        serializer = SubjectSerializer(Subject.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        subject_id = self.request.query_params.get('id', False)
        subject = Subject.objects.get(id=subject_id)

        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        subject_id = self.request.query_params.get('id', False)
        subject = Subject.objects.filter(id=subject_id)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)