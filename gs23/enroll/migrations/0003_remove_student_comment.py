# Generated by Django 3.1.5 on 2021-01-16 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_student_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='comment',
        ),
    ]
