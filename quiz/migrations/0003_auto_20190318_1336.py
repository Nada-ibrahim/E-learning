# Generated by Django 2.1.7 on 2019-03-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20190318_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default='mcq', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
