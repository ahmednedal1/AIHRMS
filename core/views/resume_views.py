from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import ResumeSerializer


@api_view(["POST"])
def upload_resume(request):
    serializer = ResumeSerializer(
        data=request.data,
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)