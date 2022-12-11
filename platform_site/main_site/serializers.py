from rest_framework import serializers
from .models import *
from django.db.models import Avg
from statistics import mean
import numpy as np
import json
from rest_framework import filters


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"


class CreateCompanySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Company
        fields = "__all__"


class AllCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    type_of_skills = serializers.CharField(source='get_type_of_skills_display')

    class Meta:
        model = Tags
        fields = "__all__"


class CompanyProjectsSerializer(serializers.ModelSerializer):
    company_requirements = TagsSerializer(many=True, read_only=True)
    company = CompanySerializer(read_only=True)
    class Meta:
        model = CompanyProjects
        fields = "__all__"


class DefaultUserSerializer(serializers.ModelSerializer):
    group = serializers.CharField(source='get_group_display')

    class Meta:
        model = DefaultUser
        fields = ("id", "username", "phone", "email", "group")


class AllStudentsSerializer(serializers.ModelSerializer):
    def get_mean_score(self, req):
        mean_work_speed = Rate.objects.values("identification_student")\
            .annotate(mean_speed=Avg("work_speed"),
                      mean_communcation=Avg("communication"),
                      mean_tech_part=Avg("tech_part"))

        for i in range(len(mean_work_speed)):
            dic = mean_work_speed[i]
            speed = dic["mean_speed"]
            communcation = dic["mean_communcation"]
            tech_part = dic["mean_tech_part"]
            mean_score = mean([speed, communcation, tech_part])
            dic["mean_score"] = np.around(float(mean_score), 2)
            dic["identification_student"] = DefaultUser.objects.get(email_user=dic["identification_student"]).pk

        needed_id = req.user.pk

        last = None
        for i in range(len(mean_work_speed)):
            if mean_work_speed[i]["identification_student"] == needed_id:
                last = mean_work_speed[i]["mean_score"]

        return last

    # user = serializers.IntegerField(source="user.pk")
    mean_rate = serializers.SerializerMethodField("get_mean_score")

    class Meta:
        model = Student
        fields = ["id", "mean_rate", "first_name", "last_name", "city_of_living"]


class StudentsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)
    user = DefaultUserSerializer(many=False, read_only=True)
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Student
        fields = "__all__"


class SortedStudentsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)
    user = DefaultUserSerializer(many=False, read_only=True)
    gender = serializers.CharField(source='get_gender_display')

    def get_mean_score(self, req):
        mean_work_speed = Rate.objects.values("identification_student")\
            .annotate(mean_speed=Avg("work_speed"),
                      mean_communcation=Avg("communication"),
                      mean_tech_part=Avg("tech_part"))

        for i in range(len(mean_work_speed)):
            dic = mean_work_speed[i]
            speed = dic["mean_speed"]
            communcation = dic["mean_communcation"]
            tech_part = dic["mean_tech_part"]
            mean_score = mean([speed, communcation, tech_part])
            dic["mean_score"] = np.around(float(mean_score), 2)
            dic["identification_student"] = DefaultUser.objects.get(email_user=dic["identification_student"]).pk

        needed_id = req.user.pk

        last = None
        for i in range(len(mean_work_speed)):
            if mean_work_speed[i]["identification_student"] == needed_id:
                last = mean_work_speed[i]["mean_score"]
                tepm_student = Student.objects.get(user_id=needed_id)
                tepm_student.mean_rate = last
                tepm_student.save()
                print("!!!!!", Student.objects.get(user_id=needed_id).mean_rate)
        return last

    mean_rate = serializers.SerializerMethodField("get_mean_score")

    class Meta:
        model = Student
        # fields = "__all__"
        fields = ["id", "mean_rate", "first_name",
                  "last_name", "city_of_living", "tags",
                  "gender", "user"]


class CreateStudentsSerializer(serializers.ModelSerializer):
    # tags = TagsSerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Student
        fields = "__all__"
        # exclude = ["user"]

class SpecificStudentsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)
    user = DefaultUserSerializer(many=False, read_only=True)

    class Meta:
        model = Student
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):
    identification_student = StudentsSerializer(many=False, read_only=True)

    class Meta:
        model = Rate
        fields = "__all__"

class CompanyBidSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBid
        fields = ["project"]

class CompanyBidUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBid
        fields = ["status", "students"]


class StudentBidSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBid
        fields = ["project", "company", "students"]


class StudentBidUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBid
        fields = ["project", "status", "company", "students"]

