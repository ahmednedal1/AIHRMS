from django.contrib import admin
from .models import Candidate, Department, JobPosition, InterviewQuestionSet, Resume, ScreeningResult



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name", "description")


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "department", "created_at")
    search_fields = ("title", "department__name")
    list_filter = ("department",)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "phone", "created_at")
    search_fields = ("full_name", "email")

    @admin.register(Resume)
    class ResumeAdmin(admin.ModelAdmin):
        list_display = ("id", "candidate", "file", "uploaded_at")
        search_fields = ("candidate__full_name",)
        list_filter = ("uploaded_at",)

    @admin.register(ScreeningResult)
    class ScreeningResultAdmin(admin.ModelAdmin):
        list_display = ("id", "candidate", "job_position", "score", "recommendation", "generated_at")
        search_fields = ("candidate__full_name", "job_position__title", "summary")
        list_filter = ("recommendation", "generated_at")

    @admin.register(InterviewQuestionSet)
    class InterviewQuestionSetAdmin(admin.ModelAdmin):
        list_display = ("id", "candidate", "job_position", "screening_result", "generated_at")
        search_fields = ("candidate__full_name", "job_position__title")
        list_filter = ("generated_at",)
# Register your models here.
