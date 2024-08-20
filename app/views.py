from django.shortcuts import render
from .models import StudentData
from django.core.serializers import serialize
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, "app/index.html")


def data(request):
    Class = StudentData.objects.values("id", "class_name")
    School = StudentData.objects.values("id", "school_name")
    AssessmentAreas = StudentData.objects.values("id", "assessment_areas")
    Student = StudentData.objects.values("id", "first_name", "last_name")
    Answers = StudentData.objects.values("id", "answers")
    Awards = StudentData.objects.values("id", "award")
    Subjects = StudentData.objects.values("id", "subject", "average_score")
    Summary = StudentData.objects.values(
        "id",
        "school_name",
        "sydney_participants",
        "sydney_percentile",
        "assessment_areas",
        "award",
        "class_name",
        "correct_answer_percentage_per_class",
        "correct_answers",
        "student_id",
        "participant",
        "student_score",
        "subject",
        "year_level",
        "answers",
        "correct_answers",
    )
    return render(
        request,
        "app/data.html",
        {
            "data1": Class,
            "data2": School,
            "data3": AssessmentAreas,
            "data4": Student,
            "data5": Answers,
            "data6": Awards,
            "data7": Subjects,
            "data8": Summary,
        },
    )
