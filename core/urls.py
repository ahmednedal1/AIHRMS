from django.urls import path
from .views import CandidateCreateView, DepartmentCreateView, JobPositionCreateView, ResumeUploadView,ScreeningResultDetailView ,InterviewQuestionSetDetailView


urlpatterns = [
    path("departments/", DepartmentCreateView.as_view(), name="department-create"),
    path("job-positions/", JobPositionCreateView.as_view(), name="job-position-create"),
    path("candidates/", CandidateCreateView.as_view(), name="candidate-create"),
    path("resumes/", ResumeUploadView.as_view(), name="resume-upload"),
    path("screening-results/<int:pk>/", ScreeningResultDetailView.as_view(), name="screening-result-detail"),
    path("interview-question-sets/<int:pk>/", InterviewQuestionSetDetailView.as_view(), name="interview-question-set-detail",
    ),

]
