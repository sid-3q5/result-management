# Generated by Django 4.0.2 on 2022-02-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'female')], max_length=6, null=True),
        ),
    ]
