# Generated by Django 4.2.1 on 2023-05-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_remove_job_category_job_experience_job_vacancy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]
