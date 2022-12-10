from django.contrib import admin

from .models import *

admin.site.register(DefaultUser)
admin.site.register(CV)
admin.site.register(Links)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Tags)
admin.site.register(Rate)
admin.site.register(CompanyProjects)
admin.site.register(StudentProjects)
admin.site.register(CompanyBid)
admin.site.register(StudentBid)
