from django.contrib import admin
from .models import Project,AboutUs,ContactUs
# Register your models here.
admin.site.register(AboutUs)
admin.site.register(Project)
admin.site.register(ContactUs)