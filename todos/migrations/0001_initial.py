# Generated by Django 3.1.1 on 2020-09-04 02:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('dateCreated', models.DateField(default=datetime.datetime.now)),
                ('dueDate', models.DateField()),
            ],
        ),
    ]