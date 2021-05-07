from django.db import models


class StationsNew(models.Model):
    # Fields
    idStations = models.AutoField('ID'),
    NameStation = models.CharField('Название', max_length=50)
    Region = models.CharField('Регион', max_length=50)
    Latitude = models.DecimalField('Широта', max_digits=5, decimal_places=2)
    Longitude = models.DecimalField('Долгота', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.NameStation

    class Meta:
        verbose_name = 'Stations'
        verbose_name_plural = 'Stations'


class MonthNew(models.Model):
    # Fields
    NameMonth = models.CharField('Месяц', max_length=50)

    def __str__(self):
        return self.MonthNew

    class Meta:
        verbose_name = 'Month'
        verbose_name_plural = 'Months'

class AlbedoNew(models.Model):
    # Fields
    Month_1 = models.DecimalField('Месяц_1', max_digits=4, decimal_places=2)
    Month_2 = models.DecimalField('Месяц_2', max_digits=4, decimal_places=2)
    Month_3 = models.DecimalField('Месяц_3', max_digits=4, decimal_places=2)
    Month_4 = models.DecimalField('Месяц_4', max_digits=4, decimal_places=2)
    Month_5 = models.DecimalField('Месяц_5', max_digits=4, decimal_places=2)
    Month_6 = models.DecimalField('Месяц_6', max_digits=4, decimal_places=2)
    Month_7 = models.DecimalField('Месяц_7', max_digits=4, decimal_places=2)
    Month_8 = models.DecimalField('Месяц_8', max_digits=4, decimal_places=2)
    Month_9 = models.DecimalField('Месяц_9', max_digits=4, decimal_places=2)
    Month_10 = models.DecimalField('Месяц_10', max_digits=4, decimal_places=2)
    Month_11 = models.DecimalField('Месяц_11', max_digits=4, decimal_places=2)
    Month_12 = models.DecimalField('Месяц_12', max_digits=4, decimal_places=2)

    def __str__(self):
        return self.AlbedoNew

    class Meta:
        verbose_name = 'Albedo'
        verbose_name_plural = 'Albedo'



class sut_sum_diff_srNew(models.Model):
    # Fields
    Month_1 = models.DecimalField('Месяц_1', max_digits=4, decimal_places=2)
    Month_2 = models.DecimalField('Месяц_2', max_digits=4, decimal_places=2)
    Month_3 = models.DecimalField('Месяц_3', max_digits=4, decimal_places=2)
    Month_4 = models.DecimalField('Месяц_4', max_digits=4, decimal_places=2)
    Month_5 = models.DecimalField('Месяц_5', max_digits=4, decimal_places=2)
    Month_6 = models.DecimalField('Месяц_6', max_digits=4, decimal_places=2)
    Month_7 = models.DecimalField('Месяц_7', max_digits=4, decimal_places=2)
    Month_8 = models.DecimalField('Месяц_8', max_digits=4, decimal_places=2)
    Month_9 = models.DecimalField('Месяц_9', max_digits=4, decimal_places=2)
    Month_10 = models.DecimalField('Месяц_10', max_digits=4, decimal_places=2)
    Month_11 = models.DecimalField('Месяц_11', max_digits=4, decimal_places=2)
    Month_12 = models.DecimalField('Месяц_12', max_digits=4, decimal_places=2)

    def __str__(self):
        return self.sut_sum_diff_srNew

    class Meta:
        verbose_name = 'sut_sum_diff_sr'
        verbose_name_plural = 'sut_sum_diff_sr'

class sut_sum_sum_srNew(models.Model):
    # Fields
    Month_1 = models.DecimalField('Месяц_1', max_digits=4, decimal_places=2)
    Month_2 = models.DecimalField('Месяц_2', max_digits=4, decimal_places=2)
    Month_3 = models.DecimalField('Месяц_3', max_digits=4, decimal_places=2)
    Month_4 = models.DecimalField('Месяц_4', max_digits=4, decimal_places=2)
    Month_5 = models.DecimalField('Месяц_5', max_digits=4, decimal_places=2)
    Month_6 = models.DecimalField('Месяц_6', max_digits=4, decimal_places=2)
    Month_7 = models.DecimalField('Месяц_7', max_digits=4, decimal_places=2)
    Month_8 = models.DecimalField('Месяц_8', max_digits=4, decimal_places=2)
    Month_9 = models.DecimalField('Месяц_9', max_digits=4, decimal_places=2)
    Month_10 = models.DecimalField('Месяц_10', max_digits=4, decimal_places=2)
    Month_11 = models.DecimalField('Месяц_11', max_digits=4, decimal_places=2)
    Month_12 = models.DecimalField('Месяц_12', max_digits=4, decimal_places=2)

    def __str__(self):
        return self.sut_sum_sum_srNew

    class Meta:
        verbose_name = 'sut_sum_sum_sr'
        verbose_name_plural = 'sut_sum_sum_sr'

class sut_sum_straight_srNew(models.Model):
    # Fields
    Month_1 = models.DecimalField('Месяц_1', max_digits=4, decimal_places=2)
    Month_2 = models.DecimalField('Месяц_2', max_digits=4, decimal_places=2)
    Month_3 = models.DecimalField('Месяц_3', max_digits=4, decimal_places=2)
    Month_4 = models.DecimalField('Месяц_4', max_digits=4, decimal_places=2)
    Month_5 = models.DecimalField('Месяц_5', max_digits=4, decimal_places=2)
    Month_6 = models.DecimalField('Месяц_6', max_digits=4, decimal_places=2)
    Month_7 = models.DecimalField('Месяц_7', max_digits=4, decimal_places=2)
    Month_8 = models.DecimalField('Месяц_8', max_digits=4, decimal_places=2)
    Month_9 = models.DecimalField('Месяц_9', max_digits=4, decimal_places=2)
    Month_10 = models.DecimalField('Месяц_10', max_digits=4, decimal_places=2)
    Month_11 = models.DecimalField('Месяц_11', max_digits=4, decimal_places=2)
    Month_12 = models.DecimalField('Месяц_12', max_digits=4, decimal_places=2)

    def __str__(self):
        return self.sut_sum_straight_srNew

    class Meta:
        verbose_name = 'sut_sum_straight_sr'
        verbose_name_plural = 'sut_sum_straight_sr'



class hour_sum_sum_srNew(models.Model):
    # Fields
    IdStations = models.IntegerField('ID Станции')
    IdHour = models.IntegerField('ID Месяца')
    Month_1 = models.DecimalField('Месяц_1', max_digits=5, decimal_places=2)
    Month_2 = models.DecimalField('Месяц_2', max_digits=5, decimal_places=2)
    Month_3 = models.DecimalField('Месяц_3', max_digits=5, decimal_places=2)
    Month_4 = models.DecimalField('Месяц_4', max_digits=5, decimal_places=2)
    Month_5 = models.DecimalField('Месяц_5', max_digits=5, decimal_places=2)
    Month_6 = models.DecimalField('Месяц_6', max_digits=5, decimal_places=2)
    Month_7 = models.DecimalField('Месяц_7', max_digits=5, decimal_places=2)
    Month_8 = models.DecimalField('Месяц_8', max_digits=5, decimal_places=2)
    Month_9 = models.DecimalField('Месяц_9', max_digits=5, decimal_places=2)
    Month_10 = models.DecimalField('Месяц_10', max_digits=5, decimal_places=2)
    Month_11 = models.DecimalField('Месяц_11', max_digits=5, decimal_places=2)
    Month_12 = models.DecimalField('Месяц_12', max_digits=5, decimal_places=2)


    def __str__(self):
        return self.hour_sum_sum_srNew

    class Meta:
        verbose_name = 'hour_sum_sum_sr'
        verbose_name_plural = 'hour_sum_sum_sr'



class hour_sum_straight_srNew(models.Model):
    # Fields
    IdStations = models.IntegerField('ID Станции')
    IdHour = models.IntegerField('ID Месяца')
    Month_1 = models.DecimalField('Месяц_1', max_digits=5, decimal_places=2)
    Month_2 = models.DecimalField('Месяц_2', max_digits=5, decimal_places=2)
    Month_3 = models.DecimalField('Месяц_3', max_digits=5, decimal_places=2)
    Month_4 = models.DecimalField('Месяц_4', max_digits=5, decimal_places=2)
    Month_5 = models.DecimalField('Месяц_5', max_digits=5, decimal_places=2)
    Month_6 = models.DecimalField('Месяц_6', max_digits=5, decimal_places=2)
    Month_7 = models.DecimalField('Месяц_7', max_digits=5, decimal_places=2)
    Month_8 = models.DecimalField('Месяц_8', max_digits=5, decimal_places=2)
    Month_9 = models.DecimalField('Месяц_9', max_digits=5, decimal_places=2)
    Month_10 = models.DecimalField('Месяц_10', max_digits=5, decimal_places=2)
    Month_11 = models.DecimalField('Месяц_11', max_digits=5, decimal_places=2)
    Month_12 = models.DecimalField('Месяц_12', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.hour_sum_straight_srNew

    class Meta:
        verbose_name = 'hour_sum_straight_sr'
        verbose_name_plural = 'hour_sum_straight_sr'



class hour_sum_diff_srNew(models.Model):
    # Fields
    IdStations = models.IntegerField('ID Станции')
    IdHour = models.IntegerField('ID Месяца')
    Month_1 = models.DecimalField('Месяц_1', max_digits=5, decimal_places=2)
    Month_2 = models.DecimalField('Месяц_2', max_digits=5, decimal_places=2)
    Month_3 = models.DecimalField('Месяц_3', max_digits=5, decimal_places=2)
    Month_4 = models.DecimalField('Месяц_4', max_digits=5, decimal_places=2)
    Month_5 = models.DecimalField('Месяц_5', max_digits=5, decimal_places=2)
    Month_6 = models.DecimalField('Месяц_6', max_digits=5, decimal_places=2)
    Month_7 = models.DecimalField('Месяц_7', max_digits=5, decimal_places=2)
    Month_8 = models.DecimalField('Месяц_8', max_digits=5, decimal_places=2)
    Month_9 = models.DecimalField('Месяц_9', max_digits=5, decimal_places=2)
    Month_10 = models.DecimalField('Месяц_10', max_digits=5, decimal_places=2)
    Month_11 = models.DecimalField('Месяц_11', max_digits=5, decimal_places=2)
    Month_12 = models.DecimalField('Месяц_12', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.hour_sum_diff_srNew

    class Meta:
        verbose_name = 'hour_sum_diff_sr'
        verbose_name_plural = 'hour_sum_diff_sr'


class mes_sum_diff_srNew(models.Model):
    # Fields
    Month_1 = models.DecimalField('Месяц_1', max_digits=5, decimal_places=2)
    Month_2 = models.DecimalField('Месяц_2', max_digits=5, decimal_places=2)
    Month_3 = models.DecimalField('Месяц_3', max_digits=5, decimal_places=2)
    Month_4 = models.DecimalField('Месяц_4', max_digits=5, decimal_places=2)
    Month_5 = models.DecimalField('Месяц_5', max_digits=5, decimal_places=2)
    Month_6 = models.DecimalField('Месяц_6', max_digits=5, decimal_places=2)
    Month_7 = models.DecimalField('Месяц_7', max_digits=5, decimal_places=2)
    Month_8 = models.DecimalField('Месяц_8', max_digits=5, decimal_places=2)
    Month_9 = models.DecimalField('Месяц_9', max_digits=5, decimal_places=2)
    Month_10 = models.DecimalField('Месяц_10', max_digits=5, decimal_places=2)
    Month_11 = models.DecimalField('Месяц_11', max_digits=5, decimal_places=2)
    Month_12 = models.DecimalField('Месяц_12', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.mes_sum_diff_srNew

    class Meta:
        verbose_name = 'mes_sum_diff_srNew'
        verbose_name_plural = 'mes_sum_diff_srNew'

class mes_sum_straight_srNew(models.Model):
    # Fields
    Month_1 = models.DecimalField('Месяц_1', max_digits=5, decimal_places=2)
    Month_2 = models.DecimalField('Месяц_2', max_digits=5, decimal_places=2)
    Month_3 = models.DecimalField('Месяц_3', max_digits=5, decimal_places=2)
    Month_4 = models.DecimalField('Месяц_4', max_digits=5, decimal_places=2)
    Month_5 = models.DecimalField('Месяц_5', max_digits=5, decimal_places=2)
    Month_6 = models.DecimalField('Месяц_6', max_digits=5, decimal_places=2)
    Month_7 = models.DecimalField('Месяц_7', max_digits=5, decimal_places=2)
    Month_8 = models.DecimalField('Месяц_8', max_digits=5, decimal_places=2)
    Month_9 = models.DecimalField('Месяц_9', max_digits=5, decimal_places=2)
    Month_10 = models.DecimalField('Месяц_10', max_digits=5, decimal_places=2)
    Month_11 = models.DecimalField('Месяц_11', max_digits=5, decimal_places=2)
    Month_12 = models.DecimalField('Месяц_12', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.mes_sum_straight_srNew

    class Meta:
        verbose_name = 'mes_sum_straight_srNew'
        verbose_name_plural = 'mes_sum_straight_srNew'

class mes_sum_sum_srNew(models.Model):
    # Fields
    Month_1 = models.DecimalField('Месяц_1', max_digits=5, decimal_places=2)
    Month_2 = models.DecimalField('Месяц_2', max_digits=5, decimal_places=2)
    Month_3 = models.DecimalField('Месяц_3', max_digits=5, decimal_places=2)
    Month_4 = models.DecimalField('Месяц_4', max_digits=5, decimal_places=2)
    Month_5 = models.DecimalField('Месяц_5', max_digits=5, decimal_places=2)
    Month_6 = models.DecimalField('Месяц_6', max_digits=5, decimal_places=2)
    Month_7 = models.DecimalField('Месяц_7', max_digits=5, decimal_places=2)
    Month_8 = models.DecimalField('Месяц_8', max_digits=5, decimal_places=2)
    Month_9 = models.DecimalField('Месяц_9', max_digits=5, decimal_places=2)
    Month_10 = models.DecimalField('Месяц_10', max_digits=5, decimal_places=2)
    Month_11 = models.DecimalField('Месяц_11', max_digits=5, decimal_places=2)
    Month_12 = models.DecimalField('Месяц_12', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.mes_sum_sum_srNew

    class Meta:
        verbose_name = 'mes_sum_sum_srNew'
        verbose_name_plural = 'mes_sum_sum_srNew'