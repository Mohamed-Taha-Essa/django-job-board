 # Generated by Django 4.2.1 on 2023-05-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_rename_descreption_job_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
