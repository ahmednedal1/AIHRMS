from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import ScreeningResult
from ..serializers import ScreeningResultSerializer


@api_view(["GET", "HEAD"])
def screening_result_detail(request, pk):
    result = get_object_or_404(ScreeningResult, pk=pk)
    serializer = ScreeningResultSerializer(result)
    return Response(serializer.data)