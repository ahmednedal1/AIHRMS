from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CandidateSerializer, DepartmentSerializer,JobPositionSerializer,ResumeSerializer, ScreeningResultSerializer, InterviewQuestionSetSerializer
from django.shortcuts import get_object_or_404
from .models import ScreeningResult
from .models import InterviewQuestionSet


class DepartmentCreateView(APIView):
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class JobPositionCreateView(APIView):
    def post(self, request):
        serializer = JobPositionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CandidateCreateView(APIView):
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)





class ResumeUploadView(APIView):
    def post(self, request):
        serializer = ResumeSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ScreeningResultDetailView(APIView):
    def get(self, request, pk):
        result = get_object_or_404(ScreeningResult, pk=pk)
        serializer = ScreeningResultSerializer(result)
        return Response(serializer.data)

class InterviewQuestionSetDetailView(APIView):
    def get(self, request, pk):
        question_set = get_object_or_404(InterviewQuestionSet, pk=pk)
        serializer = InterviewQuestionSetSerializer(question_set)
        return Response(serializer.data)
