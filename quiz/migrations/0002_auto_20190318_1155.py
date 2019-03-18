# Generated by Django 2.1.7 on 2019-03-18 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pass_score', models.IntegerField(default=0)),
                ('num_of_questions', models.IntegerField(default=1)),
                ('expected_duration', models.IntegerField(default=10)),
                ('skill_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.SkillType')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer_id',
            field=models.IntegerField(default=0),
        ),
    ]
