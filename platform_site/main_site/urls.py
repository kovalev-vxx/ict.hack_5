from django.urls import path, include, re_path
from .views import *


app_name = "main_site"


urlpatterns = [
    path('company_projects/', CompanyProjectsAPIView.as_view()),
    path('company_projects/<int:pk>/', DetailCompanyProjectsAPIView.as_view()),
    path('update_company_projects/<int:pk>/', UpdateProjectCompany.as_view()),
    path('delete_company_projects/<int:pk>/', DeleteProjectCompany.as_view()),
    path('create_company_projects/', CreateProjectCompany.as_view()),

    # для авторизованных
    path('create_company/', CreateCompanyAPIView.as_view()),
    path('update_company/<int:pk>/', UpdateCompanyAPIView.as_view()),
    path('delete_company/<int:pk>/', DeleteCompanyAPIView.as_view()),
    # для всех
    path('all_company/', AllCompanyAPIView.as_view()),
    path('all_company/<int:pk>/', AllDetailCompanyAPIView.as_view()),

    # для админа
    path('students/', AdminStudentsAPIView.as_view()),
    # для авторизованных
    path('create_student/', CreateStudentAPIView.as_view()),
    path('students/<int:pk>/', DetailStudentsAPIView.as_view()),
    path('sorted_student_by/', GetStudentsByRateAPIView.as_view()),
    path('tags_student/', GetStudentsByTagAPIViews.as_view()),
    # для всех
    path('all_students/', AllStudentsAPIView.as_view()),
    path('all_students/<int:pk>/', AllDetailStudentsAPIView.as_view()),


    path('get_mean_score/', GetMeanScore.as_view()),
    path('tags_student/', GetTagsAPIView.as_view()),
]
