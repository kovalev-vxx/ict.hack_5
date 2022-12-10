from rest_framework import generics
from .serializers import *
from rest_framework import filters
from .models import *


class ProjectsAPIView(generics.ListAPIView):
    queryset = CompanyProjects.objects.all()
    serializer_class = ProjectsSerializer


class AllStudentsAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


class GetStudentsByRateAPIView(generics.ListAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["work_speed", "communication", "tech_part"]


class GetStudentsByTagAPIViews(generics.ListAPIView):
    serializer_class = StudentsSerializer

    def get_queryset(self):
        # all_student = Student.objects.all()
        required_name_tags = self.request.query_params.getlist('tags[]')
        required_tags = []
        for required_name_tag in required_name_tags:
            required_tags.append(Tags.objects.get(name_tag=required_name_tag).pk)

        tags = []
        queryset = Student.objects.get(tags=required_tags[0])
        for tag in tags:
            queryset |= Student.objects.filter(tags=tag)

        print(queryset)
        if len(queryset):
            print("**********", queryset)
            return queryset

        return queryset
