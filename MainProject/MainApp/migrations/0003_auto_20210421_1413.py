# Generated by Django 3.1.6 on 2021-04-21 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20210416_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hour_sum_diff_srnew',
            old_name='IdMonth',
            new_name='IdHour',
        ),
        migrations.RenameField(
            model_name='hour_sum_straight_srnew',
            old_name='IdMonth',
            new_name='IdHour',
        ),
        migrations.RenameField(
            model_name='hour_sum_sum_srnew',
            old_name='IdMonth',
            new_name='IdHour',
        ),
    ]
