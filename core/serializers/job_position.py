from rest_framework import serializers
from ..models import JobPosition

class JobPositionSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(read_only=True, source='department.name')
    class Meta:
        model = JobPosition
        fields = [
            "id",
            "department",
            "department_name",
            "title",
            "description",
            "required_skills",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
