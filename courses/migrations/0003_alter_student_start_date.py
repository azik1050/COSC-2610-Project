# Generated by Django 5.1.3 on 2024-12-07 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_student_middlename_alter_student_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 12, 7, 21, 3, 45, 762801, tzinfo=datetime.timezone.utc)),
        ),
    ]
