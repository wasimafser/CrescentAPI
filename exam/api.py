from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


class ExamAPI(APIView):

    def get(self, request, format=None):
        serializer = ExamSerializer(Exam.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        exam_id = self.request.query_params.get('id', False)
        exam = Exam.objects.get(id=exam_id)

        serializer = ExamSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        exam_id = self.request.query_params.get('id', False)
        exam = Exam.objects.filter(id=exam_id)
        exam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
