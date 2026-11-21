from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import InterviewQuestionSet, ScreeningResult
from .serializers import CandidateSerializer, DepartmentSerializer, InterviewQuestionSetSerializer, JobPositionSerializer, ResumeSerializer, ScreeningResultSerializer



@api_view(["POST"])
def create_department(request):
    serializer = DepartmentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def create_job_position(request):
    serializer = JobPositionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def create_candidate(request):
    serializer = CandidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(["POST"])
def upload_resume(request):
    serializer = ResumeSerializer( data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(["GET", "HEAD"])
def screening_result_detail(request, pk):
    result = get_object_or_404(ScreeningResult, pk=pk)
    serializer = ScreeningResultSerializer(result)

    return Response(serializer.data)


@api_view(["GET", "HEAD"])
def interview_question_set_detail(request, pk):
    question_set = get_object_or_404(InterviewQuestionSet, pk=pk)
    serializer = InterviewQuestionSetSerializer(question_set)


    return Response(serializer.data)