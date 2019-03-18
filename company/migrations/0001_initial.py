# Generated by Django 2.1.7 on 2019-03-18 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0003_auto_20190318_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(default='Egypt', max_length=200)),
                ('num_of_employees', models.IntegerField(default=10)),
                ('email', models.CharField(default='company@gmail.com', max_length=200)),
                ('interest_fields', models.ManyToManyField(to='quiz.SkillType')),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(default='Vacancy description', max_length=2000)),
                ('requirments', models.CharField(default='Vacancy requirments', max_length=10000)),
                ('benefits', models.CharField(max_length=500)),
                ('salary', models.IntegerField(default=1000)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('interest_field', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.SkillType')),
                ('job_type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.JobType')),
            ],
        ),
        migrations.CreateModel(
            name='VacancyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VacancyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Vacancy')),
            ],
        ),
        migrations.AddField(
            model_name='vacancyanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.VacancyQuestion'),
        ),
        migrations.AddField(
            model_name='vacancyanswer',
            name='vacancy_application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.VacancyApplication'),
        ),
    ]