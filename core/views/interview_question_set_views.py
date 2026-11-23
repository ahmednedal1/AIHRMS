from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import InterviewQuestionSet
from ..serializers import InterviewQuestionSetSerializer

@api_view(["GET", "HEAD"])
def interview_question_set_detail(request, pk):
    question_set = get_object_or_404(InterviewQuestionSet, pk=pk)
    serializer = InterviewQuestionSetSerializer(question_set)
    return Response(serializer.data)