from django.urls import path

from .views import create_candidate,create_department, create_job_position, interview_question_set_detail, screening_result_detail, upload_resume


urlpatterns = [
    path("departments/", create_department, name="department-create"),
    path("job-positions/", create_job_position, name="job-position-create"),
    path("candidates/", create_candidate, name="candidate-create"),
    path("resumes/", upload_resume, name="resume-upload"),
    path("screening-results/<int:pk>/", screening_result_detail, name="screening-result-detail"),
    path("interview-question-sets/<int:pk>/",interview_question_set_detail, name="interview-question-set-detail"),
]