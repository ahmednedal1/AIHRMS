from django.contrib.postgres.fields import ArrayField
from django.db import models

from .department import Department


class JobPosition(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    required_skills = ArrayField(models.CharField(max_length=100))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "job_positions"
        ordering = ["title" , "id"]

    def __str__(self):
        return self.title
