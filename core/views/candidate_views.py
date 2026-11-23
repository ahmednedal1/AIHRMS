from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import CandidateSerializer

@api_view(["POST"])
def create_candidate(request):
    serializer = CandidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)