# Generated by Django 4.1.1 on 2022-09-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eva_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=200)),
                ('instructor', models.CharField(max_length=200)),
                ('enroll_semester', models.CharField(max_length=30)),
                ('credit', models.FloatField()),
                ('rate', models.FloatField()),
                ('comment', models.CharField(max_length=1024)),
            ],
        ),
    ]