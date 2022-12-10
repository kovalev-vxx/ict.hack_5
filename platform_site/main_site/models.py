from django.db import models
from django.contrib.auth.models import AbstractUser, User


class DefaultUser(User):
    phone = models.CharField(max_length=30, null=False, verbose_name="Phone")
    family_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Family name")


class Links(models.Model):
    telegram = models.TextField(blank=True, null=True, verbose_name="Telegram")
    github = models.TextField(blank=True, null=True, verbose_name="Github")
    gitlab = models.TextField(blank=True, null=True, verbose_name="GitLub")
    linkedin = models.TextField(blank=True, null=True, verbose_name="LinkedIn")
    habr_career = models.TextField(blank=True, null=True, verbose_name="Habr Career")


class CV(models.Model):
    STATUS_TYPES = (
        ("A", "Access"),
        ("C", "Checking"),
    )

    hard_skills = models.TextField(null=False, verbose_name="Hard skills")
    sof_skills = models.TextField(null=False, verbose_name="Soft skills")
    degree = models.TextField(null=False, verbose_name="Degree")
    name_of_study_institution = models.TextField(null=False, verbose_name="Institution name")
    faculty = models.TextField(null=False, verbose_name="Faculty")
    data_of_end_degree = models.DateField(verbose_name="Degree end")
    photo = models.TextField(default="https://abrakadabra.fun/uploads/posts/2021-12/1640528651_6-abrakadabra-fun-p-serii-chelovek-na-avu-7.png", verbose_name="Photo")
    experience = models.TextField(null=True, verbose_name="Experience")
    status_of_check = models.CharField(max_length=15, choices=STATUS_TYPES, default="C", verbose_name="Checking status")
    link = models.ForeignKey(Links, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Links")
    project = models.JSONField(blank=True, null=True, verbose_name="Projects")


class Tags(models.Model):
    SKILL_TYPES = (
        ("H", "Hard skill"),
        ("S", "Soft skill"),
    )

    type_of_skills = models.CharField(max_length=30, choices=SKILL_TYPES, null=False, verbose_name="Skill type")
    name_tag = models.CharField(max_length=100, null=False, verbose_name="Tag")


class Company(models.Model):
    name_company = models.CharField(max_length=100, null=False, verbose_name="Name company")
    address = models.CharField(max_length=100, null=False, verbose_name="Address")
    additional_phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="Additional phone")
    logo = models.TextField(default="https://abrakadabra.fun/uploads/posts/2021-12/1640528651_6-abrakadabra-fun-p-serii-chelovek-na-avu-7.png", verbose_name="Photo")
    user = models.OneToOneField(DefaultUser, on_delete=models.CASCADE, verbose_name="User")


class Student(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )

    first_name = models.CharField(max_length=100, null=False, verbose_name="First name")
    last_name = models.CharField(max_length=100, null=False, verbose_name="Last name")
    family_name = models.CharField(max_length=100, null=True, verbose_name="Family name")
    user = models.ForeignKey(DefaultUser, on_delete=models.CASCADE, verbose_name="User")
    birthday = models.DateField(null=False, verbose_name="Birthday")
    cv = models.ForeignKey(CV, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="CV")
    city_of_living = models.CharField(max_length=100, null=False, verbose_name="City")
    isu_number = models.CharField(max_length=100, null=False, verbose_name="ISU")
    gender = models.CharField(max_length=1, choices=GENDER, null=False, verbose_name="Gender")
    tags = models.ManyToManyField(Tags, related_name="tag", verbose_name="Tags")
    is_searching = models.BooleanField(null=False, verbose_name="Searching status")



