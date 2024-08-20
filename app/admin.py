from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import StudentData


# This class defines the structure of the data that will be imported and exported for the StudentData model.
class StudentDataResource(resources.ModelResource):
    class Meta:
        model = StudentData


# This class registers the StudentData model with the Django admin site and enables import/export functionality.
@admin.register(StudentData)
class StudentDataAdmin(ImportExportModelAdmin):
    resource_class = StudentDataResource
