from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class DefaultUser(AbstractUser):
    GROUP_CHOICE = (
        ("S", "Student"),
        ("C", "Company")
    )
    group = models.CharField(max_length=1, blank=False, null=False, verbose_name="Group", choices=GROUP_CHOICE)
    phone = models.CharField(max_length=30, blank=False, null=False, verbose_name="Phone")
    family_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Family name")
    REQUIRED_FIELDS = ["phone", "username", "group", "is_staff"]
    email = models.EmailField(_('email'), unique=True)
    USERNAME_FIELD = 'email'



class Links(models.Model):
    telegram = models.TextField(blank=True, null=True, verbose_name="Telegram")
    github = models.TextField(blank=True, null=True, verbose_name="Github")
    gitlab = models.TextField(blank=True, null=True, verbose_name="GitLub")
    linkedin = models.TextField(blank=True, null=True, verbose_name="LinkedIn")
    habr_career = models.TextField(blank=True, null=True, verbose_name="Habr Career")


class CV(models.Model):
    STATUS_TYPES = (
        ("A", "Accepted"),
        ("C", "Checking"),
    )
    link_photo = "https://abrakadabra.fun/uploads/posts/2021-12/1640528651_6-abrakadabra-fun-p-serii-chelovek-na-avu-7.png"

    hard_skills = models.TextField(null=False, verbose_name="Hard skills")
    sof_skills = models.TextField(null=False, verbose_name="Soft skills")
    degree = models.TextField(null=False, verbose_name="Degree")
    name_of_study_institution = models.TextField(null=False, verbose_name="Institution name")
    faculty = models.TextField(null=False, verbose_name="Faculty")
    data_of_end_degree = models.DateField(verbose_name="Degree end")
    photo = models.TextField(default=link_photo, verbose_name="Photo")
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
    name_tag = models.CharField(max_length=100, null=False, verbose_name="Tag", unique=True)

    def __str__(self):
        return self.name_tag


class Company(models.Model):
    link_logo = "https://abrakadabra.fun/uploads/posts/2021-12/1640528651_6-abrakadabra-fun-p-serii-chelovek-na-avu-7.png"

    name_company = models.CharField(max_length=100, null=False, verbose_name="Name company")
    address = models.CharField(max_length=100, null=False, verbose_name="Address")
    additional_phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="Additional phone")
    logo = models.TextField(default=link_logo, verbose_name="Photo")
    user = models.OneToOneField(DefaultUser, on_delete=models.CASCADE, verbose_name="User")


class Student(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )

    first_name = models.CharField(max_length=100, null=False, verbose_name="First name")
    last_name = models.CharField(max_length=100, null=False, verbose_name="Last name")
    family_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Family name")
    user = models.OneToOneField(DefaultUser, on_delete=models.CASCADE,  related_name="email_user", verbose_name="Email")
    birthday = models.DateField(null=False, verbose_name="Birthday")
    cv = models.ForeignKey(CV, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="CV")
    city_of_living = models.CharField(max_length=100, null=False, verbose_name="City")
    isu_number = models.CharField(max_length=100, null=False, verbose_name="ISU")
    gender = models.CharField(max_length=1, choices=GENDER, null=False, verbose_name="Gender")
    tags = models.ManyToManyField(Tags, related_name="tag", verbose_name="Tags")
    is_searching = models.BooleanField(null=False, verbose_name="Searching status")
    motivation_letter = models.TextField(null=False, verbose_name="Motivations letter")
    mean_rate = models.FloatField(default=0, verbose_name="Mean rate")


class Rate(models.Model):
    identification_student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student")
    work_speed = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                                  null=True,
                                                  blank=True,
                                                  verbose_name='Work speed point')
    communication = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                                     null=True,
                                                     blank=True,
                                                     verbose_name='Communication point')
    tech_part = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                                 null=True,
                                                 blank=True,
                                                 verbose_name='Tech part point')



class CompanyProjects(models.Model):
    STATUS_TYPES = (
        ("A", "Accepted"),
        ("C", "Checking"),
    )

    name = models.CharField(max_length=100, null=False, verbose_name="Name")
    description = models.TextField(blank=True, null=True, verbose_name="Photo")
    fund = models.FloatField(blank=True, null=True, verbose_name="Fund")
    company_requirements = models.ManyToManyField(Tags, related_name="company_project_tag", verbose_name="Tags")
    date_start = models.DateField(null=False, verbose_name="Start date")
    date_end = models.DateField(null=False, verbose_name="End date")
    checking_status = models.CharField(max_length=1, choices=STATUS_TYPES, default="C", verbose_name="Checking status")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Company")


class CompanyBid(models.Model):
    STATUS_TYPES = (
        ("A", "Accepted"),
        ("C", "Checking"),
    )

    project = models.OneToOneField(CompanyProjects, on_delete=models.CASCADE, verbose_name="Company project")
    students = models.ManyToManyField(Student, blank=True, null=True, verbose_name="Students")
    status = models.CharField(max_length=1, choices=STATUS_TYPES, default="C", verbose_name="Checking status")
    date_start = models.DateField(auto_now_add=True)


class StudentProjects(models.Model):
    STATUS_TYPES = (
        ("A", "Accepted"),
        ("C", "Checking"),
    )

    name = models.CharField(max_length=100, null=False, verbose_name="Name")
    description = models.TextField(blank=True, null=True, verbose_name="Photo")
    fund = models.FloatField(blank=True, null=True, verbose_name="Fund")
    student_requirements = models.ManyToManyField(Tags, related_name="student_project_tag", verbose_name="Tags")
    date_start = models.DateField(null=False, verbose_name="Start date")
    date_end = models.DateField(null=False, verbose_name="End date")
    checking_status = models.CharField(max_length=1, choices=STATUS_TYPES, default="C", verbose_name="Checking status")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student")


class StudentBid(models.Model):
    STATUS_TYPES = (
        ("A", "Accepted"),
        ("C", "Checking"),
    )

    project = models.OneToOneField(StudentProjects, on_delete=models.CASCADE, verbose_name="Student project")
    company = models.OneToOneField(Company, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Company")
    students = models.ManyToManyField(Student, blank=True, null=True, verbose_name="Students")
    status = models.CharField(max_length=1, choices=STATUS_TYPES, default="C", verbose_name="Checking status")
    date_start = models.DateField(auto_now_add=True)

