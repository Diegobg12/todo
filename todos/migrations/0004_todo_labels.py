# Generated by Django 3.1.1 on 2020-09-10 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20200910_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='labels',
            field=models.ManyToManyField(related_name='labels', to='todos.Label'),
        ),
    ]
