from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import StudentData


class StudentDataResource(resources.ModelResource):
    class Meta:
        model = StudentData


@admin.register(StudentData)
class StudentDataAdmin(ImportExportModelAdmin):
    resource_class = StudentDataResource
