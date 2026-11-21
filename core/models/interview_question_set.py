from django.contrib.postgres.fields import ArrayField
from django.db import models
from .candidate import Candidate
from .job_position import JobPosition
from .screening_result import ScreeningResult

class InterviewQuestionSet(models.Model):
    candidate = models.ForeignKey( Candidate, on_delete=models.CASCADE, related_name="interview_question_sets")
    job_position = models.ForeignKey( JobPosition, on_delete=models.CASCADE, related_name="interview_question_sets")
    screening_result = models.ForeignKey( ScreeningResult, on_delete=models.CASCADE, related_name="interview_question_sets")
    technical_questions = ArrayField(models.TextField(), default=list, blank=True)
    behavioral_questions = ArrayField(models.TextField(), default=list, blank=True)
    follow_up_questions = ArrayField(models.TextField(), default=list, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "interview_question_set"
        ordering = ['-generated_at', 'id']
    def __str__(self):
        return str(self.candidate)

