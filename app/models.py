from django.db import models


# Create your models here.
class StudentData(models.Model):
    school_name = models.CharField(max_length=255)
    year = models.IntegerField(null=True, blank=True)
    student_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    year_level = models.IntegerField(null=True, blank=True)
    class_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    answers = models.TextField()
    correct_answers = models.TextField()
    question_number = models.IntegerField(null=True, blank=True)
    subject_contents = models.TextField()
    assessment_areas = models.TextField()
    sydney_correct_count_percentage = models.FloatField()
    sydney_average_score = models.FloatField()
    sydney_participants = models.IntegerField(null=True, blank=True)
    student_score = models.FloatField()
    student_total_assessed = models.IntegerField(null=True, blank=True)
    student_area_assessed_score = models.FloatField()
    total_area_assessed_score = models.FloatField()
    participant = models.IntegerField(null=True, blank=True)
    correct_answer_percentage_per_class = models.FloatField()
    average_score = models.FloatField()
    school_percentile = models.FloatField()
    sydney_percentile = models.FloatField()
    strength_status = models.CharField(max_length=50)
    high_distinct_count = models.IntegerField(null=True, blank=True)
    distinct_count = models.IntegerField(null=True, blank=True)
    credit_count = models.IntegerField(null=True, blank=True)
    participant_count = models.IntegerField(null=True, blank=True)
    award = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"



