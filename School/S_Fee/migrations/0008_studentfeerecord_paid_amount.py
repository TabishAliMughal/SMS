# Generated by Django 3.2.6 on 2022-04-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('S_Fee', '0007_studentfeerecord_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfeerecord',
            name='paid_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
