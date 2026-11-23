from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import DepartmentSerializer

@api_view(["POST"])
def create_department(request):
    serializer = DepartmentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)