# Generated by Django 4.0.2 on 2022-04-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_rename_uname_student_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='sub1',
            field=models.IntegerField(default='-', null=True),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sub2',
            field=models.IntegerField(default='-', null=True),
        ),
        migrations.AlterField(
            model_name='marks',
            name='sub3',
            field=models.IntegerField(default='-', null=True),
        ),
    ]