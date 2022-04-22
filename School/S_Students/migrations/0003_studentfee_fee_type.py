# Generated by Django 3.2.6 on 2022-04-09 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('S_Fee', '0001_initial'),
        ('S_Students', '0002_studentfee'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfee',
            name='fee_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='S_Fee.feetypes'),
            preserve_default=False,
        ),
    ]
