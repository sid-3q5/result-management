# Generated by Django 4.0.2 on 2022-03-25 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='faculty',
            field=models.CharField(choices=[('faculty', 'faculty'), ('student', 'student')], max_length=7, null=True),
        ),
    ]
