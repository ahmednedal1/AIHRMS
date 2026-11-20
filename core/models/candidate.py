from django.db import models


class Candidate(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "candidate"
        ordering = ['full_name', 'id']

    def __str__(self):
        return self.full_name