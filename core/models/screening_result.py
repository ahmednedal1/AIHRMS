from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.postgres.fields import ArrayField
from .candidate import Candidate
from .job_position import JobPosition

class ScreeningResult(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    score = models.IntegerField()
    strengths = ArrayField(models.CharField(max_length=100))
    missing_skills = ArrayField(models.CharField(max_length=100))
    recommendation = models.CharField(max_length=7,
    choices = [
        ("proceed", "Proceed"),
        ("hold", "Hold"),
        ("reject", "Reject"),
    ])
    summary = models.TextField()
    raw_report = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        db_table = "screening_results"
        ordering = ["-generated_at", "-id"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(score__gte=0, score__lte=100),
                name="screening_score_between_0_and_100",
            ),
        ]

    def __str__(self):
        return str(self.candidate)