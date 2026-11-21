from rest_framework import serializers
from ..models import Resume
from pathlib import Path

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
        read_only_fields = ('id', 'uploaded_at')

    def validate_file(self, value):
        extension = Path(value.name).suffix.lower()
        if extension not in {".pdf", ".docx", ".txt"}:
            raise serializers.ValidationError("Upload a PDF, DOCX, or TXT file.")

        return value


