# Generated by Django 4.2.7 on 2023-12-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_feedback_alter_student_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='fname',
            field=models.CharField(max_length=50),
        ),
    ]