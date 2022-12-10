from django.db import models
from django.contrib.auth.models import AbstractUser, User


class UserSite(User):
    phone = models.CharField("Телефон", max_length=30, null=False)
    family_name = models.CharField("Отчество", max_length=50, blank=True, null=True)


class Links(models.Model):
    telegram = models.TextField("Телеграм", blank=True, null=True)
    github = models.TextField("Гитхаб", blank=True, null=True)
    gitlab = models.TextField("Гитлаб", blank=True, null=True)
    linkedin = models.TextField("Линкедин", blank=True, null=True)
    habr_career = models.TextField("Хабр карьера", blank=True, null=True)


class CV(models.Model):
    status_type = (
        ("У", "Утверждено"),
        ("П", "Проверяется"),
    )

    hard_skills = models.TextField("Технические навыки", null=False)
    sof_skills = models.TextField("Мягкие навыки",  null=False)
    degree = models.TextField("Образование",  null=False)
    name_of_study_institution = models.TextField("Название учебного заведения",  null=False)
    faculty = models.TextField("Факультет",  null=False)
    data_of_end_degree = models.DateField("Дата окончание учебного заведения")
    photo = models.TextField("Ссылка на фотографию", default="https://abrakadabra.fun/uploads/posts/2021-12/1640528651_6-abrakadabra-fun-p-serii-chelovek-na-avu-7.png")
    expiriance = models.TextField("Опыт работы",  null=True)
    status_of_check = models.CharField("Статуст проверки администартором", max_length=15 ,choices=status_type, default="П")
    link = models.ForeignKey("Links", on_delete=models.SET_NULL, verbose_name="связь с ссылками на соцсети", blank=True, null=True)
    project = models.JSONField("Проекты", blank=True, null=True)


class Tags(models.Model):
    type_skill=(
        ("Х", "Харды"),
        ("М", "Мягкие"),
    )

    type_of_skills = models.CharField("тип навыка", max_length=30, choices=type_skill, null=False)
    name_teg = models.CharField("Навык тега", max_length=100, null=False)


class Company(models.Model):
    name_company = models.CharField("Название компании", max_length=100, null=False)
    address = models.CharField("Адрес компании", max_length=100, null=False)
    additional_phone = models.CharField("дополнительный телефон", max_length=30, blank=True, null=True)
    logo = models.TextField("Ссылка на логотип", default="https://abrakadabra.fun/uploads/posts/2021-12/1640528651_6-abrakadabra-fun-p-serii-chelovek-na-avu-7.png")
    username = models.OneToOneField("UserSite", on_delete=models.CASCADE, verbose_name="имя пользователя")


class Student(models.Model):
    gender_choice = (
        ("М", "Мужчина"),
        ("Ж", "Женщина"),
    )
    type_searching=(
        ("И", "В поиске"),
        ("Н", "Не в поиске"),
    )

    first_name = models.CharField("Имя", max_length=100, null=False)
    last_name = models.CharField("Фамилия", max_length=100, null=False)
    family_name = models.CharField("Отчество", max_length=100, null=True)
    username = models.ForeignKey("UserSite", on_delete=models.CASCADE, verbose_name="имя пользователя")
    day_of_birthday = models.DateField("дата рождения", null=False)
    cv = models.ForeignKey("CV", on_delete=models.SET_NULL, verbose_name="резюме", blank=True, null=True)
    city_of_living = models.CharField("город проживания", max_length=100, null=False)
    isu_number = models.CharField("Номер ИСУ", max_length=100, null=False)
    gender = models.CharField("Пол", max_length=7, choices=gender_choice, null=False)
    tags = models.ManyToManyField("Tags", related_name="Тэг")
    status_of_searching = models.CharField("Статус поиска", choices=type_searching, null=False, max_length=15)



