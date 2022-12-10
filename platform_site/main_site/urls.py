from django.urls import path, include, re_path
from .views import *


app_name = "main_site"


urlpatterns = [
    path('projects/', ProjectsAPIView.as_view()),
    path('all_students/', AllStudentsAPIView.as_view()),
    path('sorted_student_by/', GetStudentsByRateAPIView.as_view()),
    path('tags_student/', GetStudentsByTagAPIViews.as_view())
]
