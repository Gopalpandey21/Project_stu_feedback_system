# Generated by Django 4.2.7 on 2024-04-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0008_alter_faculty_pic_alter_student_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(max_length=20, null=True),
        ),
    ]