# Generated by Django 3.2.6 on 2022-04-13 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('S_Students', '0004_alter_studentfee_fee_type'),
        ('S_Fee', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeeTypes',
        ),
    ]