# Generated by Django 5.1 on 2024-08-20 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_studentdata_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='student_id',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studentdata')),
            ],
        ),
    ]
