# Generated by Django 5.1.3 on 2024-12-08 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_student_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 12, 8, 8, 27, 57, 7025, tzinfo=datetime.timezone.utc)),
        ),
    ]