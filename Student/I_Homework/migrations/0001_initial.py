# Generated by Django 3.2.6 on 2022-04-06 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('S_Students', '0001_initial'),
        ('S_Homework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentHomeworkStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='S_Homework.homework')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='S_Students.student')),
            ],
            options={
                'unique_together': {('student', 'homework')},
            },
        ),
    ]