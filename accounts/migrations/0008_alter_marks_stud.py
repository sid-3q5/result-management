# Generated by Django 4.0.2 on 2022-03-26 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='stud',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.student'),
        ),
    ]
