# Generated by Django 3.1.6 on 2021-04-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbedoNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month_1', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_1')),
                ('Month_2', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_2')),
                ('Month_3', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_3')),
                ('Month_4', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_4')),
                ('Month_5', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_5')),
                ('Month_6', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_6')),
                ('Month_7', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_7')),
                ('Month_8', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_8')),
                ('Month_9', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_9')),
                ('Month_10', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_10')),
                ('Month_11', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_11')),
                ('Month_12', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_12')),
            ],
            options={
                'verbose_name': 'Albedo',
                'verbose_name_plural': 'Albedo',
            },
        ),
        migrations.CreateModel(
            name='hour_sum_diff_srNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdStations', models.IntegerField(verbose_name='ID Станции')),
                ('IdMonth', models.IntegerField(verbose_name='ID Месяца')),
                ('Month_1', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_1')),
                ('Month_2', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_2')),
                ('Month_3', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_3')),
                ('Month_4', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_4')),
                ('Month_5', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_5')),
                ('Month_6', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_6')),
                ('Month_7', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_7')),
                ('Month_8', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_8')),
                ('Month_9', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_9')),
                ('Month_10', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_10')),
                ('Month_11', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_11')),
                ('Month_12', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_12')),
            ],
            options={
                'verbose_name': 'hour_sum_diff_sr',
                'verbose_name_plural': 'hour_sum_diff_sr',
            },
        ),
        migrations.CreateModel(
            name='hour_sum_straight_srNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdStations', models.IntegerField(verbose_name='ID Станции')),
                ('IdMonth', models.IntegerField(verbose_name='ID Месяца')),
                ('Month_1', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_1')),
                ('Month_2', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_2')),
                ('Month_3', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_3')),
                ('Month_4', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_4')),
                ('Month_5', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_5')),
                ('Month_6', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_6')),
                ('Month_7', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_7')),
                ('Month_8', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_8')),
                ('Month_9', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_9')),
                ('Month_10', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_10')),
                ('Month_11', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_11')),
                ('Month_12', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_12')),
            ],
            options={
                'verbose_name': 'hour_sum_straight_sr',
                'verbose_name_plural': 'hour_sum_straight_sr',
            },
        ),
        migrations.CreateModel(
            name='hour_sum_sum_srNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdStations', models.IntegerField(verbose_name='ID Станции')),
                ('IdMonth', models.IntegerField(verbose_name='ID Месяца')),
                ('Month_1', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_1')),
                ('Month_2', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_2')),
                ('Month_3', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_3')),
                ('Month_4', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_4')),
                ('Month_5', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_5')),
                ('Month_6', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_6')),
                ('Month_7', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_7')),
                ('Month_8', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_8')),
                ('Month_9', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_9')),
                ('Month_10', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_10')),
                ('Month_11', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_11')),
                ('Month_12', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_12')),
            ],
            options={
                'verbose_name': 'hour_sum_sum_sr',
                'verbose_name_plural': 'hour_sum_sum_sr',
            },
        ),
        migrations.CreateModel(
            name='mes_sum_diff_srNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month_1', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_1')),
                ('Month_2', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_2')),
                ('Month_3', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_3')),
                ('Month_4', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_4')),
                ('Month_5', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_5')),
                ('Month_6', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_6')),
                ('Month_7', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_7')),
                ('Month_8', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_8')),
                ('Month_9', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_9')),
                ('Month_10', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_10')),
                ('Month_11', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_11')),
                ('Month_12', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_12')),
            ],
            options={
                'verbose_name': 'mes_sum_diff_srNew',
                'verbose_name_plural': 'mes_sum_diff_srNew',
            },
        ),
        migrations.CreateModel(
            name='mes_sum_straight_srNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month_1', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_1')),
                ('Month_2', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_2')),
                ('Month_3', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_3')),
                ('Month_4', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_4')),
                ('Month_5', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_5')),
                ('Month_6', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_6')),
                ('Month_7', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_7')),
                ('Month_8', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_8')),
                ('Month_9', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_9')),
                ('Month_10', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_10')),
                ('Month_11', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_11')),
                ('Month_12', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_12')),
            ],
            options={
                'verbose_name': 'mes_sum_straight_srNew',
                'verbose_name_plural': 'mes_sum_straight_srNew',
            },
        ),
        migrations.CreateModel(
            name='mes_sum_sum_srNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month_1', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_1')),
                ('Month_2', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_2')),
                ('Month_3', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_3')),
                ('Month_4', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_4')),
                ('Month_5', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_5')),
                ('Month_6', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_6')),
                ('Month_7', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_7')),
                ('Month_8', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_8')),
                ('Month_9', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_9')),
                ('Month_10', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_10')),
                ('Month_11', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_11')),
                ('Month_12', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_12')),
            ],
            options={
                'verbose_name': 'mes_sum_sum_srNew',
                'verbose_name_plural': 'mes_sum_sum_srNew',
            },
        ),
        migrations.CreateModel(
            name='MonthNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameMonth', models.CharField(max_length=50, verbose_name='Месяц')),
            ],
            options={
                'verbose_name': 'Month',
                'verbose_name_plural': 'Months',
            },
        ),
        migrations.CreateModel(
            name='StationsNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameStation', models.CharField(max_length=50, verbose_name='Название')),
                ('Region', models.CharField(max_length=50, verbose_name='Регион')),
                ('Latitude', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Широта')),
                ('Longitude', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Stations',
                'verbose_name_plural': 'Stations',
            },
        ),
        migrations.CreateModel(
            name='sut_sum_diff_srNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month_1', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_1')),
                ('Month_2', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_2')),
                ('Month_3', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_3')),
                ('Month_4', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_4')),
                ('Month_5', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_5')),
                ('Month_6', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_6')),
                ('Month_7', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_7')),
                ('Month_8', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_8')),
                ('Month_9', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_9')),
                ('Month_10', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_10')),
                ('Month_11', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_11')),
                ('Month_12', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_12')),
            ],
            options={
                'verbose_name': 'sut_sum_diff_sr',
                'verbose_name_plural': 'sut_sum_diff_sr',
            },
        ),
        migrations.CreateModel(
            name='sut_sum_straight_srNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month_1', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_1')),
                ('Month_2', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_2')),
                ('Month_3', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_3')),
                ('Month_4', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_4')),
                ('Month_5', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_5')),
                ('Month_6', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_6')),
                ('Month_7', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_7')),
                ('Month_8', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_8')),
                ('Month_9', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_9')),
                ('Month_10', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_10')),
                ('Month_11', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_11')),
                ('Month_12', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_12')),
            ],
            options={
                'verbose_name': 'sut_sum_straight_sr',
                'verbose_name_plural': 'sut_sum_straight_sr',
            },
        ),
        migrations.CreateModel(
            name='sut_sum_sum_srNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month_1', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_1')),
                ('Month_2', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_2')),
                ('Month_3', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_3')),
                ('Month_4', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_4')),
                ('Month_5', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_5')),
                ('Month_6', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_6')),
                ('Month_7', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_7')),
                ('Month_8', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_8')),
                ('Month_9', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_9')),
                ('Month_10', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_10')),
                ('Month_11', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_11')),
                ('Month_12', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Месяц_12')),
            ],
            options={
                'verbose_name': 'sut_sum_sum_sr',
                'verbose_name_plural': 'sut_sum_sum_sr',
            },
        ),
    ]
