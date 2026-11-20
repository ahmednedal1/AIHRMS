from django.db import models

from .candidate import Candidate


class Resume(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "resumes"
        ordering = ["-uploaded_at", "-id"]

    def __str__(self):
        return self.file.name
