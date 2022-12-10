from rest_framework import serializers
from .models import *
from django.db.models import Avg

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProjects
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    type_of_skills = serializers.CharField(source='get_type_of_skills_display')

    class Meta:
        model = Tags
        fields = "__all__"


class DefaultUserSerializer(serializers.ModelSerializer):
    group = serializers.CharField(source='get_group_display')

    class Meta:
        model = DefaultUser
        fields = ("id", "username", "phone", "email", "group")


class StudentsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)
    user = DefaultUserSerializer(many=False, read_only=True)
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Student
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):
    identification_student = StudentsSerializer(many=False, read_only=True)
    mean_score = serializers.SerializerMethodField('get_mean_points')


    def get_mean_points(self, request):
        # mean_work_speed = Rate.objects.filter(pk=req.data["id"]).values("identification_student").annotate(mean_speed=Avg("work_speed"))
        return mean_work_speed

    class Meta:
        model = Rate
        fields = "__all__"
        extra_fields = ["mean_score"]


# class GetStudentsByTagSerializer(serializers.ModelSerializer):
#     pass
    #id_student =
