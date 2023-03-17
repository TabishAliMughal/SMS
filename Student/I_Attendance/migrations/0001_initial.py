# Generated by Django 3.2.6 on 2022-06-19 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('S_Students', '0004_alter_studentfee_fee_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_attendance', models.DateField()),
                ('capture_datetime', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='S_Students.student')),
            ],
        ),
    ]
