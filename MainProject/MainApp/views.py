import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import StationsNew, mes_sum_sum_srNew, mes_sum_straight_srNew, mes_sum_diff_srNew, MonthNew, AlbedoNew, sut_sum_diff_srNew, sut_sum_sum_srNew, sut_sum_straight_srNew, hour_sum_sum_srNew, hour_sum_straight_srNew, hour_sum_diff_srNew
from django.core.paginator import Paginator
from django.db.models import Q
from django.core import serializers
from geopy import distance
import operator
from collections import OrderedDict
import numpy as np

def index(request):
    return render(request, 'MainApp/index.html')


def ShowStations(request):
    stat = StationsNew.objects.all()
    paginator = Paginator(stat, 25)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'MainApp/ShowStations.html', context=context)



def FindName(request):

    return render(request, 'MainApp/FindName.html')


def FindNumber(request):
    return render(request, 'MainApp/FindNumber.html')


def FindCoord(request):
    return render(request, 'MainApp/FindCoord.html')








def SearchResult(request):
    search_query = request.GET.get('search','')
    request.session['res2'] = search_query


    search_query2 = request.GET.get('search_num', '')
    request.session['res2_num'] = search_query2
    #request.session['res1'] = search_query2

    if search_query:

        stat = StationsNew.objects.filter(NameStation=search_query)
        ser = serializers.serialize("json", stat)
        request.session['res1'] = ser

        r = StationsNew.objects.select_related('id').filter(NameStation=search_query)[:1]
        #request.session['res1'] = r

        albedo = AlbedoNew.objects.filter(id=r)
        ser1 = serializers.serialize("json", albedo)
        request.session['res_alb'] = ser1

        mes_sum = mes_sum_sum_srNew.objects.filter(id=r)
        mes_straight = mes_sum_straight_srNew.objects.filter(id=r)
        mes_diff = mes_sum_diff_srNew.objects.filter(id=r)

        sut_sum = sut_sum_sum_srNew.objects.filter(id=r)
        sut_straight = sut_sum_straight_srNew.objects.filter(id=r)
        sut_diff = sut_sum_diff_srNew.objects.filter(id=r)

        hour_sum = hour_sum_sum_srNew.objects.filter(IdStations=r)
        hour_straight = hour_sum_straight_srNew.objects.filter(IdStations=r)
        hour_diff = hour_sum_diff_srNew.objects.filter(IdStations=r)




    elif search_query2:
        stat = StationsNew.objects.filter(id=search_query2)
        ser = serializers.serialize("json", stat)
        request.session['res1'] = ser


        mes_sum = mes_sum_sum_srNew.objects.filter(id=search_query2)
        mes_straight = mes_sum_straight_srNew.objects.filter(id=search_query2)
        mes_diff = mes_sum_diff_srNew.objects.filter(id=search_query2)

        sut_sum = sut_sum_sum_srNew.objects.filter(id=search_query2)
        sut_straight = sut_sum_straight_srNew.objects.filter(id=search_query2)
        sut_diff = sut_sum_diff_srNew.objects.filter(id=search_query2)

        hour_sum = hour_sum_sum_srNew.objects.filter(IdStations=search_query2)
        hour_straight = hour_sum_straight_srNew.objects.filter(IdStations=search_query2)
        hour_diff = hour_sum_diff_srNew.objects.filter(IdStations=search_query2)

        albedo = AlbedoNew.objects.filter(id=search_query2)
        ser1 = serializers.serialize("json", albedo)
        request.session['res3'] = ser1

    else:
        stat = StationsNew.objects.all()

    context = {
        'res' : stat,
        'res_mes_sum' : mes_sum,
        'res_mes_straight' : mes_straight,
        'res_mes_diff' : mes_diff,
        'res_sut_sum' : sut_sum,
        'res_sut_straight' : sut_straight,
        'res_sut_diff' : sut_diff,
        'res_hour_sum' : hour_sum,
        'res_hour_straight' : hour_straight,
        'res_hour_diff' : hour_diff,
        'albedo': albedo
    }


    return render(request, 'MainApp/SearchResult.html', context= context)

def SearchResult_1(request):

    search_query_coord_1 = request.session.get('res_coord_1')
    if search_query_coord_1:
        stat = StationsNew.objects.filter(id=search_query_coord_1)
        ser = serializers.serialize("json", stat)
        request.session['res1'] = ser

        mes_sum = mes_sum_sum_srNew.objects.filter(id=search_query_coord_1)
        mes_straight = mes_sum_straight_srNew.objects.filter(id=search_query_coord_1)
        mes_diff = mes_sum_diff_srNew.objects.filter(id=search_query_coord_1)

        sut_sum = sut_sum_sum_srNew.objects.filter(id=search_query_coord_1)
        sut_straight = sut_sum_straight_srNew.objects.filter(id=search_query_coord_1)
        sut_diff = sut_sum_diff_srNew.objects.filter(id=search_query_coord_1)

        hour_sum = hour_sum_sum_srNew.objects.filter(IdStations=search_query_coord_1)
        hour_straight = hour_sum_straight_srNew.objects.filter(IdStations=search_query_coord_1)
        hour_diff = hour_sum_diff_srNew.objects.filter(IdStations=search_query_coord_1)

        albedo = AlbedoNew.objects.filter(id=search_query_coord_1)
        ser1 = serializers.serialize("json", albedo)
        request.session['res3'] = ser1

        context = {
            'res': stat,
            'res_mes_sum': mes_sum,
            'res_mes_straight': mes_straight,
            'res_mes_diff': mes_diff,
            'res_sut_sum': sut_sum,
            'res_sut_straight': sut_straight,
            'res_sut_diff': sut_diff,
            'res_hour_sum': hour_sum,
            'res_hour_straight': hour_straight,
            'res_hour_diff': hour_diff,
            'albedo': albedo
        }

        return render(request, 'MainApp/SearchResult_1.html', context=context)


def SearchResult_2(request):

    search_query_coord_2 = request.session.get('res_coord_2')
    if search_query_coord_2:
        stat = StationsNew.objects.filter(id=search_query_coord_2)
        ser = serializers.serialize("json", stat)
        request.session['res1'] = ser

        mes_sum = mes_sum_sum_srNew.objects.filter(id=search_query_coord_2)
        mes_straight = mes_sum_straight_srNew.objects.filter(id=search_query_coord_2)
        mes_diff = mes_sum_diff_srNew.objects.filter(id=search_query_coord_2)

        sut_sum = sut_sum_sum_srNew.objects.filter(id=search_query_coord_2)
        sut_straight = sut_sum_straight_srNew.objects.filter(id=search_query_coord_2)
        sut_diff = sut_sum_diff_srNew.objects.filter(id=search_query_coord_2)

        hour_sum = hour_sum_sum_srNew.objects.filter(IdStations=search_query_coord_2)
        hour_straight = hour_sum_straight_srNew.objects.filter(IdStations=search_query_coord_2)
        hour_diff = hour_sum_diff_srNew.objects.filter(IdStations=search_query_coord_2)

        albedo = AlbedoNew.objects.filter(id=search_query_coord_2)
        ser1 = serializers.serialize("json", albedo)
        request.session['res3'] = ser1

        context = {
            'res': stat,
            'res_mes_sum': mes_sum,
            'res_mes_straight': mes_straight,
            'res_mes_diff': mes_diff,
            'res_sut_sum': sut_sum,
            'res_sut_straight': sut_straight,
            'res_sut_diff': sut_diff,
            'res_hour_sum': hour_sum,
            'res_hour_straight': hour_straight,
            'res_hour_diff': hour_diff,
            'albedo': albedo
        }

        return render(request, 'MainApp/SearchResult_2.html', context=context)

def SearchResult_3(request):

    search_query_coord_3 = request.session.get('res_coord_3')

    if search_query_coord_3:
        stat = StationsNew.objects.filter(id=search_query_coord_3)
        ser = serializers.serialize("json", stat)
        request.session['res1'] = ser

        mes_sum = mes_sum_sum_srNew.objects.filter(id=search_query_coord_3)
        mes_straight = mes_sum_straight_srNew.objects.filter(id=search_query_coord_3)
        mes_diff = mes_sum_diff_srNew.objects.filter(id=search_query_coord_3)

        sut_sum = sut_sum_sum_srNew.objects.filter(id=search_query_coord_3)
        sut_straight = sut_sum_straight_srNew.objects.filter(id=search_query_coord_3)
        sut_diff = sut_sum_diff_srNew.objects.filter(id=search_query_coord_3)

        hour_sum = hour_sum_sum_srNew.objects.filter(IdStations=search_query_coord_3)
        hour_straight = hour_sum_straight_srNew.objects.filter(IdStations=search_query_coord_3)
        hour_diff = hour_sum_diff_srNew.objects.filter(IdStations=search_query_coord_3)

        albedo = AlbedoNew.objects.filter(id=search_query_coord_3)
        ser1 = serializers.serialize("json", albedo)
        request.session['res3'] = ser1

        context = {
            'res': stat,
            'res_mes_sum': mes_sum,
            'res_mes_straight': mes_straight,
            'res_mes_diff': mes_diff,
            'res_sut_sum': sut_sum,
            'res_sut_straight': sut_straight,
            'res_sut_diff': sut_diff,
            'res_hour_sum': hour_sum,
            'res_hour_straight': hour_straight,
            'res_hour_diff': hour_diff,
            'albedo': albedo
        }

        return render(request, 'MainApp/SearchResult_3.html', context=context)






def Export_csv(request):
    res = request.session.get('res3')
    obj = next(serializers.deserialize("json", res)).object


    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_Albedo12.csv"'
    writer.writerow(['1','2','3','4','5','6','7','8','9','10','11','12'])

    writer.writerow([obj.Month_1, obj.Month_2, obj.Month_3, obj.Month_4, obj.Month_5, obj.Month_6, obj.Month_7, obj.Month_8, obj.Month_9, obj.Month_10, obj.Month_11, obj.Month_12])

    return response


def Export_csv_sum(request):
    res = request.session.get('res2')
    res1 = request.session.get('res2_num')
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_GlobalHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res:
        r = StationsNew.objects.get(NameStation=res)
        stat = hour_sum_sum_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    elif res1:
        r = StationsNew.objects.get(id=res1)
        stat = hour_sum_sum_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    return response

def Export_csv_sum_1(request):
    res2 = request.session.get('res_coord_1')
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_GlobalHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res2:
        r = StationsNew.objects.get(id=res2)
        stat = hour_sum_sum_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    return response

def Export_csv_sum_2(request):
    res3 = request.session.get('res_coord_2')
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_GlobalHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res3:
        r = StationsNew.objects.get(id=res3)
        stat = hour_sum_sum_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    return response

def Export_csv_sum_3(request):
    res4 = request.session.get('res_coord_3')
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_GlobalHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res4:
        r = StationsNew.objects.get(id=res4)
        stat = hour_sum_sum_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])
    return response


def Export_csv_str(request):
    res = request.session.get('res2')
    res1 = request.session.get('res2_num')
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_DirectHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res:
        r = StationsNew.objects.get(NameStation=res)
        stat = hour_sum_straight_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    elif res1:
        r = StationsNew.objects.get(id=res1)
        stat = hour_sum_straight_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    return response

def Export_csv_str_1(request):

    res2 = request.session.get('res_coord_1')
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_DirectHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res2:
        r = StationsNew.objects.get(id=res2)
        stat = hour_sum_straight_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    return response

def Export_csv_str_2(request):

    res3 = request.session.get('res_coord_2')

    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_DirectHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res3:
        r = StationsNew.objects.get(id=res3)
        stat = hour_sum_straight_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    return response

def Export_csv_str_3(request):
    res4 = request.session.get('res_coord_3')
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_DirectHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res4:
        r = StationsNew.objects.get(id=res4)
        stat = hour_sum_straight_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    return response

def Export_csv_diff(request):
    res = request.session.get('res2')
    res1 = request.session.get('res2_num')
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_DiffuseHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res:
        r = StationsNew.objects.get(NameStation=res)
        stat = hour_sum_diff_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    elif res1:
        r = StationsNew.objects.get(id=res1)
        stat = hour_sum_diff_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])


    return response

def Export_csv_diff_1(request):

    res2 = request.session.get('res_coord_1')

    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_DiffuseHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res2:
        r = StationsNew.objects.get(id=res2)
        stat = hour_sum_diff_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])



    return response

def Export_csv_diff_2(request):

    res3 = request.session.get('res_coord_2')

    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_DiffuseHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res3:
        r = StationsNew.objects.get(id=res3)
        stat = hour_sum_diff_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])



    return response

def Export_csv_diff_3(request):
    res4 = request.session.get('res_coord_3')
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    response['Content-Disposition'] = 'attachment; filename = "Typical_DiffuseHI24.csv"'
    writer.writerow([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
    if res4:
        r = StationsNew.objects.get(id=res4)
        stat = hour_sum_diff_srNew.objects.filter(IdStations=r.id)
        for row in stat:
            writer.writerow(
                [row.IdHour, row.Month_1, row.Month_2, row.Month_3, row.Month_4, row.Month_5, row.Month_6, row.Month_7,
                 row.Month_8, row.Month_9, row.Month_10, row.Month_11, row.Month_12])

    return response


def Show(request):
    search_query_sr = request.GET.get('search_coord_sr', '')
    search_query_dl = request.GET.get('search_coord_dl', '')
    coords_1 = (float(search_query_sr), float(search_query_dl))
    object_list = serializers.serialize("python", StationsNew.objects.all())
    stat = []
    name={}
    name2 = {}

    i=1
    for object in object_list:

        for field_name, field_value in object['fields'].items():
            if field_name == 'Latitude':
               a = field_value
            if field_name == 'Longitude':
                b = field_value

        coords_2 = (float(a), float(b))
        dist = distance.distance(coords_1, coords_2).km

        name[i] = dist
        i=i+1

    name2 = sorted(name.items(), key=operator.itemgetter(1))[:3]

    n1 = (name2[0])[0]
    n2 = (name2[1])[0]
    n3 = (name2[2])[0]

    request.session['res_coord_1'] = n1
    request.session['res_coord_2'] = n2
    request.session['res_coord_3'] = n3

    stat1 = StationsNew.objects.get(id=n1)
    stat2 = StationsNew.objects.get(id=n2)
    stat3 = StationsNew.objects.get(id=n3)



    return render(request, 'MainApp/Show.html', context={ 'n1':format((name2[0])[1], '.2f'), 'n2':format((name2[1])[1], '.2f'),'n3':format((name2[2])[1], '.2f'), 'res':stat1, 'res2':stat2, 'res3':stat3})

def Export(request):

    return render(request, 'MainApp/Export.html')



def Ex(request):
    res = request.session.get('res2')
    res1 = request.session.get('res2_num')
    if res:
        r = StationsNew.objects.get(NameStation=res)

    if res1:
        r = StationsNew.objects.get(id=res1)

    stat = AlbedoNew.objects.filter(id=r.id)
    stat1 = hour_sum_sum_srNew.objects.filter(IdStations=r.id)
    stat2 = hour_sum_straight_srNew.objects.filter(IdStations=r.id)
    stat3 = hour_sum_diff_srNew.objects.filter(IdStations=r.id)

    hour = []
    for i  in range(365):
        for j in range(1, 25):
            hour.append(j)

    day = []
    for i in range(1, 13):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            for j in range(1, 32):
                for k in range(24):
                    day.append(j)
        elif i in [4, 6, 9, 11]:
            for j in range(1, 31):
                for k in range(24):
                    day.append(j)
        elif i == 2:
            for j in range(1, 29):
                for k in range(24):
                    day.append(j)

    month = []
    for i in range(1, 13):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            for j in range(31):
                for k in range(24):
                    month.append(i)
        elif i in [4, 6, 9, 11]:
            for j in range(30):
                for k in range(24):
                    month.append(i)
        elif i == 2:
            for j in range(28):
                for k in range(24):
                    month.append(i)

    DOY = []
    for i in range(1, 366):
        for j in range(24):
            DOY.append(i)

    HOY = []
    for i in range(1, 8761):
        HOY.append(i)

    ind = []
    for i in range(4380):
        ind.append(i)

    per = []
    for i in range(8760):
        per.append(i)
    del per[::2]

    #res2 = request.session.get('res_coord_1')
    #res3 = request.session.get('res_coord_2')
    #res4 = request.session.get('res_coord_3')

    a = []
    a1 = []
    a2 = []
    a3 = []
    a11 = []
    a12 = []
    a13 = []
    a14 = []
    a15 = []
    a16 = []
    a17 = []
    a18 = []
    a19 = []
    a110 = []
    a111 = []
    a112 = []

    object_list = serializers.serialize("python", stat)
    object_list1 = serializers.serialize("python", stat1)
    object_list2 = serializers.serialize("python", stat2)
    object_list3 = serializers.serialize("python", stat3)


    Period = request.GET.get('Period')
    Type = request.GET.get('Type')
    Hour = request.GET.get('Hour')

    # Тип интерполяции - "День сурка"
    if Type == 'Type_surok':
        # Заполнение массивов
        for object in object_list:
            for field_name, field_value in object['fields'].items():
                if field_name == 'Month_1':
                    for i in range(744):
                        a.append(float(field_value))
                if field_name == 'Month_2':
                    for i in range(672):
                        a.append(float(field_value))
                if field_name == 'Month_3':
                    for i in range(744):
                        a.append(float(field_value))
                if field_name == 'Month_4':
                    for i in range(720):
                        a.append(float(field_value))
                if field_name == 'Month_5':
                    for i in range(744):
                        a.append(float(field_value))
                if field_name == 'Month_6':
                    for i in range(720):
                        a.append(float(field_value))
                if field_name == 'Month_7':
                    for i in range(744):
                        a.append(float(field_value))
                if field_name == 'Month_8':
                    for i in range(744):
                        a.append(float(field_value))
                if field_name == 'Month_9':
                    for i in range(720):
                        a.append(float(field_value))
                if field_name == 'Month_10':
                    for i in range(744):
                        a.append(float(field_value))
                if field_name == 'Month_11':
                    for i in range(720):
                        a.append(float(field_value))
                if field_name == 'Month_12':
                    for i in range(744):
                        a.append(float(field_value))

        for object in object_list1:
            for field_name, field_value in object['fields'].items():
                if field_name == 'Month_1':
                    a11.append(float(field_value))

                if field_name == 'Month_2':
                    a12.append(float(field_value))

                if field_name == 'Month_3':
                    a13.append(float(field_value))

                if field_name == 'Month_4':
                    a14.append(float(field_value))

                if field_name == 'Month_5':
                    a15.append(float(field_value))

                if field_name == 'Month_6':
                    a16.append(float(field_value))

                if field_name == 'Month_7':
                    a17.append(float(field_value))

                if field_name == 'Month_8':
                    a18.append(float(field_value))

                if field_name == 'Month_9':
                    a19.append(float(field_value))

                if field_name == 'Month_10':
                    a110.append(float(field_value))

                if field_name == 'Month_11':
                    a111.append(float(field_value))

                if field_name == 'Month_12':
                    a112.append(float(field_value))

        a1 = a11 * 31 + a12 * 28 + a13 * 31 + a14 * 30 + a15 * 31 + a16 * 30 + a17 * 31 + a18 * 31 + a19 * 30 + a110 * 31 + a111 * 30 + a112 * 31

        a11.clear()
        a12.clear()
        a13.clear()
        a14.clear()
        a15.clear()
        a16.clear()
        a17.clear()
        a18.clear()
        a19.clear()
        a110.clear()
        a111.clear()
        a112.clear()

        for object in object_list2:
            for field_name, field_value in object['fields'].items():
                if field_name == 'Month_1':
                    a11.append(float(field_value))

                if field_name == 'Month_2':
                    a12.append(float(field_value))

                if field_name == 'Month_3':
                    a13.append(float(field_value))

                if field_name == 'Month_4':
                    a14.append(float(field_value))

                if field_name == 'Month_5':
                    a15.append(float(field_value))

                if field_name == 'Month_6':
                    a16.append(float(field_value))

                if field_name == 'Month_7':
                    a17.append(float(field_value))

                if field_name == 'Month_8':
                    a18.append(float(field_value))

                if field_name == 'Month_9':
                    a19.append(float(field_value))

                if field_name == 'Month_10':
                    a110.append(float(field_value))

                if field_name == 'Month_11':
                    a111.append(float(field_value))

                if field_name == 'Month_12':
                    a112.append(float(field_value))

        a2 = a11 * 31 + a12 * 28 + a13 * 31 + a14 * 30 + a15 * 31 + a16 * 30 + a17 * 31 + a18 * 31 + a19 * 30 + a110 * 31 + a111 * 30 + a112 * 31

        a11.clear()
        a12.clear()
        a13.clear()
        a14.clear()
        a15.clear()
        a16.clear()
        a17.clear()
        a18.clear()
        a19.clear()
        a110.clear()
        a111.clear()
        a112.clear()

        for object in object_list3:
            for field_name, field_value in object['fields'].items():
                if field_name == 'Month_1':
                    a11.append(float(field_value))

                if field_name == 'Month_2':
                    a12.append(float(field_value))

                if field_name == 'Month_3':
                    a13.append(float(field_value))

                if field_name == 'Month_4':
                    a14.append(float(field_value))

                if field_name == 'Month_5':
                    a15.append(float(field_value))

                if field_name == 'Month_6':
                    a16.append(float(field_value))

                if field_name == 'Month_7':
                    a17.append(float(field_value))

                if field_name == 'Month_8':
                    a18.append(float(field_value))

                if field_name == 'Month_9':
                    a19.append(float(field_value))

                if field_name == 'Month_10':
                    a110.append(float(field_value))

                if field_name == 'Month_11':
                    a111.append(float(field_value))

                if field_name == 'Month_12':
                    a112.append(float(field_value))

        a3 = a11 * 31 + a12 * 28 + a13 * 31 + a14 * 30 + a15 * 31 + a16 * 30 + a17 * 31 + a18 * 31 + a19 * 30 + a110 * 31 + a111 * 30 + a112 * 31

        # Данные за весь период
        if Period == 'All_period':
        # Шаг дискретизации 1 час
            if Hour == 'Hour_1':

                response = HttpResponse(content_type='text/csv')
                writer = csv.writer(response)
                response['Content-Disposition'] = 'attachment; filename = "sum.csv"'

                writer.writerow([' ', 'HOY', 'DOY', 'Month', 'Day', 'Hour', 'GHI', 'DHI', 'DirectHI', 'Albedo'])

                for i in range(8760):
                    writer.writerow([i, HOY[i], DOY[i], month[i], day[i], hour[i], a1[i], a3[i], a2[i], a[i]])

            # Шаг дискретизации 2 часа
            if Hour == 'Hour_2':

                response = HttpResponse(content_type='text/csv')
                writer = csv.writer(response)
                response['Content-Disposition'] = 'attachment; filename = "sum.csv"'

                writer.writerow([' ', 'HOY', 'DOY', 'Month', 'Day', 'Hour', 'GHI', 'DHI', 'DirectHI', 'Albedo'])

                j = 0
                for i in per:
                    writer.writerow([j, HOY[i], DOY[i], month[i], day[i], hour[i], a1[i], a3[i], a2[i], a[i]])
                    j = j+1
    # Данные за указанный интервал
        if Period == 'Part_Period':
            Mes_begin = request.GET.get('Mes_begin')
            Day_begin = request.GET.get('Day_begin')
            Hour_begin = request.GET.get('Hour_begin')

            Mes_end = request.GET.get('Mes_end')
            Day_end = request.GET.get('Day_end')
            Hour_end = request.GET.get('Hour_end')

            sum_begin = 0
            sum_end = 0

            for i in range(1, int(Mes_begin)):
                if i in [1, 3, 5, 7, 8, 10, 12]:
                    sum_begin = sum_begin + 744
                if i == 2:
                    sum_begin = sum_begin + 672
                if i in [4, 6, 9, 11]:
                    sum_begin = sum_begin + 720

            sum_begin = sum_begin + int((int(Day_begin)-1)*24)
            sum_begin = sum_begin + int(Hour_begin)

            for i in range(1, int(Mes_end)):
                if i in [1, 3, 5, 7, 8, 10, 12]:
                    sum_end = sum_end + 744
                if i == 2:
                    sum_end = sum_end + 672
                if i in [4, 6, 9, 11]:
                    sum_end = sum_end + 720

            sum_end = sum_end + int((int(Day_end)-1)*24)
            sum_end = sum_end + int(Hour_end)


            # Шаг дискретизации 1 час
            if Hour == 'Hour_1':

                response = HttpResponse(content_type='text/csv')
                writer = csv.writer(response)
                response['Content-Disposition'] = 'attachment; filename = "sum.csv"'

                writer.writerow([' ', 'HOY', 'DOY', 'Month', 'Day', 'Hour', 'GHI', 'DHI', 'DirectHI', 'Albedo'])
                j = 0
                for i in range(sum_begin-1, sum_end):
                    writer.writerow([j, HOY[i], DOY[i], month[i], day[i], hour[i], a1[i], a3[i], a2[i], a[i]])
                    j = j+1

            # Шаг дискретизации 2 часа
            if Hour == 'Hour_2':

                response = HttpResponse(content_type='text/csv')
                writer = csv.writer(response)
                response['Content-Disposition'] = 'attachment; filename = "sum.csv"'

                writer.writerow([' ', 'HOY', 'DOY', 'Month', 'Day', 'Hour', 'GHI', 'DHI', 'DirectHI', 'Albedo'])
                j = 0
                for i in per:
                    if i in range(sum_begin-1, sum_end+1):
                        writer.writerow([j, HOY[i], DOY[i], month[i], day[i], hour[i], a1[i], a3[i], a2[i], a[i]])
                        j = j+1

# Тип интерполяции - линейная
    if Type == 'Type_lin':
        a21 = []
        a22 = []
        a23 = []
        a24 = []
        a25 = []
        a26 = []
        a27 = []
        a28 = []
        a29 = []
        a210 = []
        a211 = []
        a212 = []

        # Заполнение массивов
        for object in object_list:
            for field_name, field_value in object['fields'].items():
                if field_name == 'Month_1':
                    a11.append(float(field_value))
                if field_name == 'Month_2':
                    a12.append(float(field_value))
                if field_name == 'Month_3':
                    a13.append(float(field_value))
                if field_name == 'Month_4':
                    a14.append(float(field_value))
                if field_name == 'Month_5':
                    a15.append(float(field_value))
                if field_name == 'Month_6':
                    a16.append(float(field_value))
                if field_name == 'Month_7':
                    a17.append(float(field_value))
                if field_name == 'Month_8':
                    a18.append(float(field_value))
                if field_name == 'Month_9':
                    a19.append(float(field_value))
                if field_name == 'Month_10':
                    a110.append(float(field_value))
                if field_name == 'Month_11':
                    a111.append(float(field_value))
                if field_name == 'Month_12':
                    a112.append(float(field_value))
        # 1
        for i in range(1):
            if a11[i] > a12[i]:
                raz = a11[i] - a12[i]
                delt = float(raz / 744)
                k = a11[i]
                for j in range(744):
                    k = k - delt
                    a21.append(float("{0:.3f}".format(k)))
            elif a11[i] < a12[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 744)
                k = a11[i]
                for j in range(744):
                    k = k + delt
                    a21.append(float("{0:.3f}".format(k)))
            elif a11[i] == a12[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 744)
                k = a11[i]
                for j in range(744):
                    k = k + delt
                    a21.append(float("{0:.3f}".format(k)))
        # 2
        for i in range(1):
            if a12[i] > a13[i]:
                raz = a12[i] - a13[i]
                delt = float(raz / 672)
                k = a12[i]
                for j in range(672):
                    k = k - delt
                    a22.append(float("{0:.3f}".format(k)))
            elif a12[i] < a13[i]:
                raz = a13[i] - a12[i]
                delt = float(raz / 672)
                k = a12[i]
                for j in range(672):
                    k = k + delt
                    a22.append(float("{0:.3f}".format(k)))
            elif a12[i] == a13[i]:
                raz = a13[i] - a12[i]
                delt = float(raz / 672)
                k = a12[i]
                for j in range(672):
                    k = k + delt
                    a22.append(float("{0:.3f}".format(k)))
        # 3
        for i in range(1):
            if a13[i] > a14[i]:
                raz = a13[i] - a14[i]
                delt = float(raz / 744)
                k = a13[i]
                for j in range(744):
                    k = k - delt
                    a23.append(float("{0:.3f}".format(k)))
            elif a13[i] < a14[i]:
                raz = a14[i] - a13[i]
                delt = float(raz / 744)
                k = a13[i]
                for j in range(744):
                    k = k + delt
                    a23.append(float("{0:.3f}".format(k)))
            elif a13[i] == a14[i]:
                raz = a14[i] - a13[i]
                delt = float(raz / 744)
                k = a11[i]
                for j in range(744):
                    k = k + delt
                    a23.append(float("{0:.3f}".format(k)))
        # 4
        for i in range(1):
            if a14[i] > a15[i]:
                raz = a14[i] - a15[i]
                delt = float(raz / 720)
                k = a14[i]
                for j in range(720):
                    k = k - delt
                    a24.append(float("{0:.3f}".format(k)))
            elif a14[i] < a15[i]:
                raz = a15[i] - a14[i]
                delt = float(raz / 720)
                k = a14[i]
                for j in range(720):
                    k = k + delt
                    a24.append(float("{0:.3f}".format(k)))
            elif a14[i] == a15[i]:
                raz = a15[i] - a14[i]
                delt = float(raz / 720)
                k = a14[i]
                for j in range(720):
                    k = k + delt
                    a24.append(float("{0:.3f}".format(k)))
        # 5
        for i in range(1):
            if a15[i] > a16[i]:
                raz = a15[i] - a16[i]
                delt = float(raz / 744)
                k = a15[i]
                for j in range(744):
                    k = k - delt
                    a25.append(float("{0:.3f}".format(k)))
            elif a15[i] < a16[i]:
                raz = a16[i] - a15[i]
                delt = float(raz / 744)
                k = a15[i]
                for j in range(744):
                    k = k + delt
                    a25.append(float("{0:.3f}".format(k)))
            elif a15[i] == a16[i]:
                raz = a16[i] - a15[i]
                delt = float(raz / 744)
                k = a15[i]
                for j in range(744):
                    k = k + delt
                    a25.append(float("{0:.3f}".format(k)))
        # 6
        for i in range(1):
            if a16[i] > a17[i]:
                raz = a16[i] - a17[i]
                delt = float(raz / 720)
                k = a16[i]
                for j in range(720):
                    k = k - delt
                    a26.append(float("{0:.3f}".format(k)))
            elif a16[i] < a17[i]:
                raz = a17[i] - a16[i]
                delt = float(raz / 720)
                k = a16[i]
                for j in range(720):
                    k = k + delt
                    a26.append(float("{0:.3f}".format(k)))
            elif a16[i] == a17[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 720)
                k = a16[i]
                for j in range(720):
                    k = k + delt
                    a26.append(float("{0:.3f}".format(k)))
        # 7
        for i in range(1):
            if a17[i] > a18[i]:
                raz = a17[i] - a18[i]
                delt = float(raz / 744)
                k = a17[i]
                for j in range(744):
                    k = k - delt
                    a27.append(float("{0:.3f}".format(k)))
            elif a17[i] < a18[i]:
                raz = a18[i] - a17[i]
                delt = float(raz / 744)
                k = a17[i]
                for j in range(744):
                    k = k + delt
                    a27.append(float("{0:.3f}".format(k)))
            elif a17[i] == a18[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 744)
                k = a17[i]
                for j in range(744):
                    k = k + delt
                    a27.append(float("{0:.3f}".format(k)))
        # 8
        for i in range(1):
            if a18[i] > a19[i]:
                raz = a18[i] - a19[i]
                delt = float(raz / 744)
                k = a18[i]
                for j in range(744):
                    k = k - delt
                    a28.append(float("{0:.3f}".format(k)))
            elif a18[i] < a19[i]:
                raz = a19[i] - a18[i]
                delt = float(raz / 744)
                k = a18[i]
                for j in range(744):
                    k = k + delt
                    a28.append(float("{0:.3f}".format(k)))
            elif a18[i] == a19[i]:
                raz = a19[i] - a18[i]
                delt = float(raz / 744)
                k = a18[i]
                for j in range(744):
                    k = k + delt
                    a28.append(float("{0:.3f}".format(k)))
        # 9
        for i in range(1):
            if a19[i] > a110[i]:
                raz = a19[i] - a110[i]
                delt = float(raz / 720)
                k = a19[i]
                for j in range(720):
                    k = k - delt
                    a29.append(float("{0:.3f}".format(k)))
            elif a19[i] < a110[i]:
                raz = a110[i] - a19[i]
                delt = float(raz / 720)
                k = a19[i]
                for j in range(720):
                    k = k + delt
                    a29.append(float("{0:.3f}".format(k)))
            elif a19[i] == a110[i]:
                raz = a110[i] - a19[i]
                delt = float(raz / 720)
                k = a19[i]
                for j in range(720):
                    k = k + delt
                    a29.append(float("{0:.3f}".format(k)))
        # 10
        for i in range(1):
            if a110[i] > a111[i]:
                raz = a110[i] - a111[i]
                delt = float(raz / 744)
                k = a110[i]
                for j in range(744):
                    k = k - delt
                    a210.append(float("{0:.3f}".format(k)))
            elif a110[i] < a111[i]:
                raz = a111[i] - a110[i]
                delt = float(raz / 744)
                k = a110[i]
                for j in range(744):
                    k = k + delt
                    a210.append(float("{0:.3f}".format(k)))
            elif a110[i] == a111[i]:
                raz = a111[i] - a110[i]
                delt = float(raz / 744)
                k = a110[i]
                for j in range(744):
                    k = k + delt
                    a210.append(float("{0:.3f}".format(k)))
        # 11
        for i in range(1):
            if a111[i] > a112[i]:
                raz = a111[i] - a112[i]
                delt = float(raz / 720)
                k = a111[i]
                for j in range(720):
                    k = k - delt
                    a211.append(float("{0:.3f}".format(k)))
            elif a111[i] < a112[i]:
                raz = a112[i] - a111[i]
                delt = float(raz / 720)
                k = a111[i]
                for j in range(720):
                    k = k + delt
                    a211.append(float("{0:.3f}".format(k)))
            elif a111[i] == a112[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 720)
                k = a111[i]
                for j in range(720):
                    k = k + delt
                    a211.append(float("{0:.3f}".format(k)))
        # 12
        for i in range(1):
            if a112[i] > a11[i]:
                raz = a112[i] - a11[i]
                delt = float(raz / 744)
                k = a112[i]
                for j in range(744):
                    k = k - delt
                    a212.append(float("{0:.3f}".format(k)))
            elif a112[i] < a11[i]:
                raz = a11[i] - a112[i]
                delt = float(raz / 744)
                k = a112[i]
                for j in range(744):
                    k = k + delt
                    a212.append(float("{0:.3f}".format(k)))
            elif a112[i] == a11[i]:
                raz = a11[i] - a112[i]
                delt = float(raz / 744)
                k = a112[i]
                for j in range(744):
                    k = k + delt
                    a212.append(float("{0:.3f}".format(k)))

        begin = []
        for i in range(336):
            begin.append(a212[i])
        end = []
        for i in range(336, 744):
            end.append(a212[i])

        a = begin + a21 + a22 + a23 + a24 + a25 + a26 + a27 + a28 + a29 + a210 + a211 + end

        a11.clear()
        a12.clear()
        a13.clear()
        a14.clear()
        a15.clear()
        a16.clear()
        a17.clear()
        a18.clear()
        a19.clear()
        a110.clear()
        a111.clear()
        a112.clear()
        a21.clear()
        a22.clear()
        a23.clear()
        a24.clear()
        a25.clear()
        a26.clear()
        a27.clear()
        a28.clear()
        a29.clear()
        a210.clear()
        a211.clear()
        a212.clear()
        begin.clear()
        end.clear()


        for object in object_list1:
            for field_name, field_value in object['fields'].items():
                if field_name == 'Month_1':
                    a11.append(float(field_value))
                if field_name == 'Month_2':
                    a12.append(float(field_value))
                if field_name == 'Month_3':
                    a13.append(float(field_value))
                if field_name == 'Month_4':
                    a14.append(float(field_value))
                if field_name == 'Month_5':
                    a15.append(float(field_value))
                if field_name == 'Month_6':
                    a16.append(float(field_value))
                if field_name == 'Month_7':
                    a17.append(float(field_value))
                if field_name == 'Month_8':
                    a18.append(float(field_value))
                if field_name == 'Month_9':
                    a19.append(float(field_value))
                if field_name == 'Month_10':
                    a110.append(float(field_value))
                if field_name == 'Month_11':
                    a111.append(float(field_value))
                if field_name == 'Month_12':
                    a112.append(float(field_value))
    #1
        for i in range(24):
            if a11[i] > a12[i]:
                raz = a11[i] - a12[i]
                delt = float(raz/31)
                k = a11[i]
                for j in range(31):
                    k = k - delt
                    a21.append(float("{0:.3f}".format(k)))
            elif a11[i] < a12[i]:
                raz = a12[i] - a11[i]
                delt = float(raz/31)
                k = a11[i]
                for j in range(31):
                    k = k + delt
                    a21.append(float("{0:.3f}".format(k)))
            elif a11[i] == a12[i]:
                raz = a12[i] - a11[i]
                delt = float(raz/31)
                k = a11[i]
                for j in range(31):
                    k = k + delt
                    a21.append(float("{0:.3f}".format(k)))
    #2
        for i in range(24):
            if a12[i] > a13[i]:
                raz = a12[i] - a13[i]
                delt = float(raz/28)
                k = a12[i]
                for j in range(28):
                    k = k - delt
                    a22.append(float("{0:.3f}".format(k)))
            elif a12[i] < a13[i]:
                raz = a13[i] - a12[i]
                delt = float(raz/28)
                k = a12[i]
                for j in range(28):
                    k = k + delt
                    a22.append(float("{0:.3f}".format(k)))
            elif a12[i] == a13[i]:
                raz = a13[i] - a12[i]
                delt = float(raz/28)
                k = a12[i]
                for j in range(28):
                    k = k + delt
                    a22.append(float("{0:.3f}".format(k)))
    #3
        for i in range(24):
            if a13[i] > a14[i]:
                raz = a13[i] - a14[i]
                delt = float(raz/31)
                k = a13[i]
                for j in range(31):
                    k = k - delt
                    a23.append(float("{0:.3f}".format(k)))
            elif a13[i] < a14[i]:
                raz = a14[i] - a13[i]
                delt = float(raz/31)
                k = a13[i]
                for j in range(31):
                    k = k + delt
                    a23.append(float("{0:.3f}".format(k)))
            elif a13[i] == a14[i]:
                raz = a14[i] - a13[i]
                delt = float(raz/31)
                k = a11[i]
                for j in range(31):
                    k = k + delt
                    a23.append(float("{0:.3f}".format(k)))
    #4
        for i in range(24):
            if a14[i] > a15[i]:
                raz = a14[i] - a15[i]
                delt = float(raz/30)
                k = a14[i]
                for j in range(30):
                    k = k - delt
                    a24.append(float("{0:.3f}".format(k)))
            elif a14[i] < a15[i]:
                raz = a15[i] - a14[i]
                delt = float(raz/30)
                k = a14[i]
                for j in range(30):
                    k = k + delt
                    a24.append(float("{0:.3f}".format(k)))
            elif a14[i] == a15[i]:
                raz = a15[i] - a14[i]
                delt = float(raz/30)
                k = a14[i]
                for j in range(30):
                    k = k + delt
                    a24.append(float("{0:.3f}".format(k)))
    #5
        for i in range(24):
            if a15[i] > a16[i]:
                raz = a15[i] - a16[i]
                delt = float(raz/31)
                k = a15[i]
                for j in range(31):
                    k = k - delt
                    a25.append(float("{0:.3f}".format(k)))
            elif a15[i] < a16[i]:
                raz = a16[i] - a15[i]
                delt = float(raz/31)
                k = a15[i]
                for j in range(31):
                    k = k + delt
                    a25.append(float("{0:.3f}".format(k)))
            elif a15[i] == a16[i]:
                raz = a16[i] - a15[i]
                delt = float(raz/31)
                k = a15[i]
                for j in range(31):
                    k = k + delt
                    a25.append(float("{0:.3f}".format(k)))
    #6
        for i in range(24):
            if a16[i] > a17[i]:
                raz = a16[i] - a17[i]
                delt = float(raz/30)
                k = a16[i]
                for j in range(30):
                    k = k - delt
                    a26.append(float("{0:.3f}".format(k)))
            elif a16[i] < a17[i]:
                raz = a17[i] - a16[i]
                delt = float(raz/30)
                k = a16[i]
                for j in range(30):
                    k = k + delt
                    a26.append(float("{0:.3f}".format(k)))
            elif a16[i] == a17[i]:
                raz = a12[i] - a11[i]
                delt = float(raz/30)
                k = a16[i]
                for j in range(30):
                    k = k + delt
                    a26.append(float("{0:.3f}".format(k)))
    #7
        for i in range(24):
            if a17[i] > a18[i]:
                raz = a17[i] - a18[i]
                delt = float(raz/31)
                k = a17[i]
                for j in range(31):
                    k = k - delt
                    a27.append(float("{0:.3f}".format(k)))
            elif a17[i] < a18[i]:
                raz = a18[i] - a17[i]
                delt = float(raz/31)
                k = a17[i]
                for j in range(31):
                    k = k + delt
                    a27.append(float("{0:.3f}".format(k)))
            elif a17[i] == a18[i]:
                raz = a12[i] - a11[i]
                delt = float(raz/31)
                k = a17[i]
                for j in range(31):
                    k = k + delt
                    a27.append(float("{0:.3f}".format(k)))
    #8
        for i in range(24):
            if a18[i] > a19[i]:
                raz = a18[i] - a19[i]
                delt = float(raz/31)
                k = a18[i]
                for j in range(31):
                    k = k - delt
                    a28.append(float("{0:.3f}".format(k)))
            elif a18[i] < a19[i]:
                raz = a19[i] - a18[i]
                delt = float(raz/31)
                k = a18[i]
                for j in range(31):
                    k = k + delt
                    a28.append(float("{0:.3f}".format(k)))
            elif a18[i] == a19[i]:
                raz = a19[i] - a18[i]
                delt = float(raz/31)
                k = a18[i]
                for j in range(31):
                    k = k + delt
                    a28.append(float("{0:.3f}".format(k)))
    #9
        for i in range(24):
            if a19[i] > a110[i]:
                raz = a19[i] - a110[i]
                delt = float(raz/30)
                k = a19[i]
                for j in range(30):
                    k = k - delt
                    a29.append(float("{0:.3f}".format(k)))
            elif a19[i] < a110[i]:
                raz = a110[i] - a19[i]
                delt = float(raz/30)
                k = a19[i]
                for j in range(30):
                    k = k + delt
                    a29.append(float("{0:.3f}".format(k)))
            elif a19[i] == a110[i]:
                raz = a110[i] - a19[i]
                delt = float(raz/30)
                k = a19[i]
                for j in range(30):
                    k = k + delt
                    a29.append(float("{0:.3f}".format(k)))
    #10
        for i in range(24):
            if a110[i] > a111[i]:
                raz = a110[i] - a111[i]
                delt = float(raz/31)
                k = a110[i]
                for j in range(31):
                    k = k - delt
                    a210.append(float("{0:.3f}".format(k)))
            elif a110[i] < a111[i]:
                raz = a111[i] - a110[i]
                delt = float(raz/31)
                k = a110[i]
                for j in range(31):
                    k = k + delt
                    a210.append(float("{0:.3f}".format(k)))
            elif a110[i] == a111[i]:
                raz = a111[i] - a110[i]
                delt = float(raz/31)
                k = a110[i]
                for j in range(31):
                    k = k + delt
                    a210.append(float("{0:.3f}".format(k)))
    #11
        for i in range(24):
            if a111[i] > a112[i]:
                raz = a111[i] - a112[i]
                delt = float(raz/30)
                k = a111[i]
                for j in range(30):
                    k = k - delt
                    a211.append(float("{0:.3f}".format(k)))
            elif a111[i] < a112[i]:
                raz = a112[i] - a111[i]
                delt = float(raz/30)
                k = a111[i]
                for j in range(30):
                    k = k + delt
                    a211.append(float("{0:.3f}".format(k)))
            elif a111[i] == a112[i]:
                raz = a12[i] - a11[i]
                delt = float(raz/30)
                k = a111[i]
                for j in range(30):
                    k = k + delt
                    a211.append(float("{0:.3f}".format(k)))
    #12
        for i in range(24):
            if a112[i] > a11[i]:
                raz = a112[i] - a11[i]
                delt = float(raz/31)
                k = a112[i]
                for j in range(31):
                    k = k - delt
                    a212.append(float("{0:.3f}".format(k)))
            elif a112[i] < a11[i]:
                raz = a11[i] - a112[i]
                delt = float(raz/31)
                k = a112[i]
                for j in range(31):
                    k = k + delt
                    a212.append(float("{0:.3f}".format(k)))
            elif a112[i] == a11[i]:
                raz = a11[i] - a112[i]
                delt = float(raz/31)
                k = a112[i]
                for j in range(31):
                    k = k + delt
                    a212.append(float("{0:.3f}".format(k)))

        begin = []
        for i in range(336):
            begin.append(a212[i])
        end = []
        for i in range(336, 744):
            end.append(a212[i])

        a1 = begin + a21 + a22 + a23 + a24 + a25 + a26 + a27 + a28 + a29 + a210 + a211 + end

        a11.clear()
        a12.clear()
        a13.clear()
        a14.clear()
        a15.clear()
        a16.clear()
        a17.clear()
        a18.clear()
        a19.clear()
        a110.clear()
        a111.clear()
        a112.clear()
        a21.clear()
        a22.clear()
        a23.clear()
        a24.clear()
        a25.clear()
        a26.clear()
        a27.clear()
        a28.clear()
        a29.clear()
        a210.clear()
        a211.clear()
        a212.clear()
        begin.clear()
        end.clear()

        for object in object_list2:
            for field_name, field_value in object['fields'].items():
                if field_name == 'Month_1':
                    a11.append(float(field_value))
                if field_name == 'Month_2':
                    a12.append(float(field_value))
                if field_name == 'Month_3':
                    a13.append(float(field_value))
                if field_name == 'Month_4':
                    a14.append(float(field_value))
                if field_name == 'Month_5':
                    a15.append(float(field_value))
                if field_name == 'Month_6':
                    a16.append(float(field_value))
                if field_name == 'Month_7':
                    a17.append(float(field_value))
                if field_name == 'Month_8':
                    a18.append(float(field_value))
                if field_name == 'Month_9':
                    a19.append(float(field_value))
                if field_name == 'Month_10':
                    a110.append(float(field_value))
                if field_name == 'Month_11':
                    a111.append(float(field_value))
                if field_name == 'Month_12':
                    a112.append(float(field_value))
        # 1
        for i in range(24):
            if a11[i] > a12[i]:
                raz = a11[i] - a12[i]
                delt = float(raz / 31)
                k = a11[i]
                for j in range(31):
                    k = k - delt
                    a21.append(float("{0:.3f}".format(k)))
            elif a11[i] < a12[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 31)
                k = a11[i]
                for j in range(31):
                    k = k + delt
                    a21.append(float("{0:.3f}".format(k)))
            elif a11[i] == a12[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 31)
                k = a11[i]
                for j in range(31):
                    k = k + delt
                    a21.append(float("{0:.3f}".format(k)))
        # 2
        for i in range(24):
            if a12[i] > a13[i]:
                raz = a12[i] - a13[i]
                delt = float(raz / 28)
                k = a12[i]
                for j in range(28):
                    k = k - delt
                    a22.append(float("{0:.3f}".format(k)))
            elif a12[i] < a13[i]:
                raz = a13[i] - a12[i]
                delt = float(raz / 28)
                k = a12[i]
                for j in range(28):
                    k = k + delt
                    a22.append(float("{0:.3f}".format(k)))
            elif a12[i] == a13[i]:
                raz = a13[i] - a12[i]
                delt = float(raz / 28)
                k = a12[i]
                for j in range(28):
                    k = k + delt
                    a22.append(float("{0:.3f}".format(k)))
        # 3
        for i in range(24):
            if a13[i] > a14[i]:
                raz = a13[i] - a14[i]
                delt = float(raz / 31)
                k = a13[i]
                for j in range(31):
                    k = k - delt
                    a23.append(float("{0:.3f}".format(k)))
            elif a13[i] < a14[i]:
                raz = a14[i] - a13[i]
                delt = float(raz / 31)
                k = a13[i]
                for j in range(31):
                    k = k + delt
                    a23.append(float("{0:.3f}".format(k)))
            elif a13[i] == a14[i]:
                raz = a14[i] - a13[i]
                delt = float(raz / 31)
                k = a11[i]
                for j in range(31):
                    k = k + delt
                    a23.append(float("{0:.3f}".format(k)))
        # 4
        for i in range(24):
            if a14[i] > a15[i]:
                raz = a14[i] - a15[i]
                delt = float(raz / 30)
                k = a14[i]
                for j in range(30):
                    k = k - delt
                    a24.append(float("{0:.3f}".format(k)))
            elif a14[i] < a15[i]:
                raz = a15[i] - a14[i]
                delt = float(raz / 30)
                k = a14[i]
                for j in range(30):
                    k = k + delt
                    a24.append(float("{0:.3f}".format(k)))
            elif a14[i] == a15[i]:
                raz = a15[i] - a14[i]
                delt = float(raz / 30)
                k = a14[i]
                for j in range(30):
                    k = k + delt
                    a24.append(float("{0:.3f}".format(k)))
        # 5
        for i in range(24):
            if a15[i] > a16[i]:
                raz = a15[i] - a16[i]
                delt = float(raz / 31)
                k = a15[i]
                for j in range(31):
                    k = k - delt
                    a25.append(float("{0:.3f}".format(k)))
            elif a15[i] < a16[i]:
                raz = a16[i] - a15[i]
                delt = float(raz / 31)
                k = a15[i]
                for j in range(31):
                    k = k + delt
                    a25.append(float("{0:.3f}".format(k)))
            elif a15[i] == a16[i]:
                raz = a16[i] - a15[i]
                delt = float(raz / 31)
                k = a15[i]
                for j in range(31):
                    k = k + delt
                    a25.append(float("{0:.3f}".format(k)))
        # 6
        for i in range(24):
            if a16[i] > a17[i]:
                raz = a16[i] - a17[i]
                delt = float(raz / 30)
                k = a16[i]
                for j in range(30):
                    k = k - delt
                    a26.append(float("{0:.3f}".format(k)))
            elif a16[i] < a17[i]:
                raz = a17[i] - a16[i]
                delt = float(raz / 30)
                k = a16[i]
                for j in range(30):
                    k = k + delt
                    a26.append(float("{0:.3f}".format(k)))
            elif a16[i] == a17[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 30)
                k = a16[i]
                for j in range(30):
                    k = k + delt
                    a26.append(float("{0:.3f}".format(k)))
        # 7
        for i in range(24):
            if a17[i] > a18[i]:
                raz = a17[i] - a18[i]
                delt = float(raz / 31)
                k = a17[i]
                for j in range(31):
                    k = k - delt
                    a27.append(float("{0:.3f}".format(k)))
            elif a17[i] < a18[i]:
                raz = a18[i] - a17[i]
                delt = float(raz / 31)
                k = a17[i]
                for j in range(31):
                    k = k + delt
                    a27.append(float("{0:.3f}".format(k)))
            elif a17[i] == a18[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 31)
                k = a17[i]
                for j in range(31):
                    k = k + delt
                    a27.append(float("{0:.3f}".format(k)))
        # 8
        for i in range(24):
            if a18[i] > a19[i]:
                raz = a18[i] - a19[i]
                delt = float(raz / 31)
                k = a18[i]
                for j in range(31):
                    k = k - delt
                    a28.append(float("{0:.3f}".format(k)))
            elif a18[i] < a19[i]:
                raz = a19[i] - a18[i]
                delt = float(raz / 31)
                k = a18[i]
                for j in range(31):
                    k = k + delt
                    a28.append(float("{0:.3f}".format(k)))
            elif a18[i] == a19[i]:
                raz = a19[i] - a18[i]
                delt = float(raz / 31)
                k = a18[i]
                for j in range(31):
                    k = k + delt
                    a28.append(float("{0:.3f}".format(k)))
        # 9
        for i in range(24):
            if a19[i] > a110[i]:
                raz = a19[i] - a110[i]
                delt = float(raz / 30)
                k = a19[i]
                for j in range(30):
                    k = k - delt
                    a29.append(float("{0:.3f}".format(k)))
            elif a19[i] < a110[i]:
                raz = a110[i] - a19[i]
                delt = float(raz / 30)
                k = a19[i]
                for j in range(30):
                    k = k + delt
                    a29.append(float("{0:.3f}".format(k)))
            elif a19[i] == a110[i]:
                raz = a110[i] - a19[i]
                delt = float(raz / 30)
                k = a19[i]
                for j in range(30):
                    k = k + delt
                    a29.append(float("{0:.3f}".format(k)))
        # 10
        for i in range(24):
            if a110[i] > a111[i]:
                raz = a110[i] - a111[i]
                delt = float(raz / 31)
                k = a110[i]
                for j in range(31):
                    k = k - delt
                    a210.append(float("{0:.3f}".format(k)))
            elif a110[i] < a111[i]:
                raz = a111[i] - a110[i]
                delt = float(raz / 31)
                k = a110[i]
                for j in range(31):
                    k = k + delt
                    a210.append(float("{0:.3f}".format(k)))
            elif a110[i] == a111[i]:
                raz = a111[i] - a110[i]
                delt = float(raz / 31)
                k = a110[i]
                for j in range(31):
                    k = k + delt
                    a210.append(float("{0:.3f}".format(k)))
        # 11
        for i in range(24):
            if a111[i] > a112[i]:
                raz = a111[i] - a112[i]
                delt = float(raz / 30)
                k = a111[i]
                for j in range(30):
                    k = k - delt
                    a211.append(float("{0:.3f}".format(k)))
            elif a111[i] < a112[i]:
                raz = a112[i] - a111[i]
                delt = float(raz / 30)
                k = a111[i]
                for j in range(30):
                    k = k + delt
                    a211.append(float("{0:.3f}".format(k)))
            elif a111[i] == a112[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 30)
                k = a111[i]
                for j in range(30):
                    k = k + delt
                    a211.append(float("{0:.3f}".format(k)))
        # 12
        for i in range(24):
            if a112[i] > a11[i]:
                raz = a112[i] - a11[i]
                delt = float(raz / 31)
                k = a112[i]
                for j in range(31):
                    k = k - delt
                    a212.append(float("{0:.3f}".format(k)))
            elif a112[i] < a11[i]:
                raz = a11[i] - a112[i]
                delt = float(raz / 31)
                k = a112[i]
                for j in range(31):
                    k = k + delt
                    a212.append(float("{0:.3f}".format(k)))
            elif a112[i] == a11[i]:
                raz = a11[i] - a112[i]
                delt = float(raz / 31)
                k = a112[i]
                for j in range(31):
                    k = k + delt
                    a212.append(float("{0:.3f}".format(k)))

        begin = []
        for i in range(336):
            begin.append(a212[i])
        end = []
        for i in range(336, 744):
            end.append(a212[i])

        a2 = begin + a21 + a22 + a23 + a24 + a25 + a26 + a27 + a28 + a29 + a210 + a211 + end

        a11.clear()
        a12.clear()
        a13.clear()
        a14.clear()
        a15.clear()
        a16.clear()
        a17.clear()
        a18.clear()
        a19.clear()
        a110.clear()
        a111.clear()
        a112.clear()
        a21.clear()
        a22.clear()
        a23.clear()
        a24.clear()
        a25.clear()
        a26.clear()
        a27.clear()
        a28.clear()
        a29.clear()
        a210.clear()
        a211.clear()
        a212.clear()
        begin.clear()
        end.clear()

        for object in object_list3:
            for field_name, field_value in object['fields'].items():
                if field_name == 'Month_1':
                    a11.append(float(field_value))
                if field_name == 'Month_2':
                    a12.append(float(field_value))
                if field_name == 'Month_3':
                    a13.append(float(field_value))
                if field_name == 'Month_4':
                    a14.append(float(field_value))
                if field_name == 'Month_5':
                    a15.append(float(field_value))
                if field_name == 'Month_6':
                    a16.append(float(field_value))
                if field_name == 'Month_7':
                    a17.append(float(field_value))
                if field_name == 'Month_8':
                    a18.append(float(field_value))
                if field_name == 'Month_9':
                    a19.append(float(field_value))
                if field_name == 'Month_10':
                    a110.append(float(field_value))
                if field_name == 'Month_11':
                    a111.append(float(field_value))
                if field_name == 'Month_12':
                    a112.append(float(field_value))
        # 1
        for i in range(24):
            if a11[i] > a12[i]:
                raz = a11[i] - a12[i]
                delt = float(raz / 31)
                k = a11[i]
                for j in range(31):
                    k = k - delt
                    a21.append(float("{0:.3f}".format(k)))
            elif a11[i] < a12[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 31)
                k = a11[i]
                for j in range(31):
                    k = k + delt
                    a21.append(float("{0:.3f}".format(k)))
            elif a11[i] == a12[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 31)
                k = a11[i]
                for j in range(31):
                    k = k + delt
                    a21.append(float("{0:.3f}".format(k)))
        # 2
        for i in range(24):
            if a12[i] > a13[i]:
                raz = a12[i] - a13[i]
                delt = float(raz / 28)
                k = a12[i]
                for j in range(28):
                    k = k - delt
                    a22.append(float("{0:.3f}".format(k)))
            elif a12[i] < a13[i]:
                raz = a13[i] - a12[i]
                delt = float(raz / 28)
                k = a12[i]
                for j in range(28):
                    k = k + delt
                    a22.append(float("{0:.3f}".format(k)))
            elif a12[i] == a13[i]:
                raz = a13[i] - a12[i]
                delt = float(raz / 28)
                k = a12[i]
                for j in range(28):
                    k = k + delt
                    a22.append(float("{0:.3f}".format(k)))
        # 3
        for i in range(24):
            if a13[i] > a14[i]:
                raz = a13[i] - a14[i]
                delt = float(raz / 31)
                k = a13[i]
                for j in range(31):
                    k = k - delt
                    a23.append(float("{0:.3f}".format(k)))
            elif a13[i] < a14[i]:
                raz = a14[i] - a13[i]
                delt = float(raz / 31)
                k = a13[i]
                for j in range(31):
                    k = k + delt
                    a23.append(float("{0:.3f}".format(k)))
            elif a13[i] == a14[i]:
                raz = a14[i] - a13[i]
                delt = float(raz / 31)
                k = a11[i]
                for j in range(31):
                    k = k + delt
                    a23.append(float("{0:.3f}".format(k)))
        # 4
        for i in range(24):
            if a14[i] > a15[i]:
                raz = a14[i] - a15[i]
                delt = float(raz / 30)
                k = a14[i]
                for j in range(30):
                    k = k - delt
                    a24.append(float("{0:.3f}".format(k)))
            elif a14[i] < a15[i]:
                raz = a15[i] - a14[i]
                delt = float(raz / 30)
                k = a14[i]
                for j in range(30):
                    k = k + delt
                    a24.append(float("{0:.3f}".format(k)))
            elif a14[i] == a15[i]:
                raz = a15[i] - a14[i]
                delt = float(raz / 30)
                k = a14[i]
                for j in range(30):
                    k = k + delt
                    a24.append(float("{0:.3f}".format(k)))
        # 5
        for i in range(24):
            if a15[i] > a16[i]:
                raz = a15[i] - a16[i]
                delt = float(raz / 31)
                k = a15[i]
                for j in range(31):
                    k = k - delt
                    a25.append(float("{0:.3f}".format(k)))
            elif a15[i] < a16[i]:
                raz = a16[i] - a15[i]
                delt = float(raz / 31)
                k = a15[i]
                for j in range(31):
                    k = k + delt
                    a25.append(float("{0:.3f}".format(k)))
            elif a15[i] == a16[i]:
                raz = a16[i] - a15[i]
                delt = float(raz / 31)
                k = a15[i]
                for j in range(31):
                    k = k + delt
                    a25.append(float("{0:.3f}".format(k)))
        # 6
        for i in range(24):
            if a16[i] > a17[i]:
                raz = a16[i] - a17[i]
                delt = float(raz / 30)
                k = a16[i]
                for j in range(30):
                    k = k - delt
                    a26.append(float("{0:.3f}".format(k)))
            elif a16[i] < a17[i]:
                raz = a17[i] - a16[i]
                delt = float(raz / 30)
                k = a16[i]
                for j in range(30):
                    k = k + delt
                    a26.append(float("{0:.3f}".format(k)))
            elif a16[i] == a17[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 30)
                k = a16[i]
                for j in range(30):
                    k = k + delt
                    a26.append(float("{0:.3f}".format(k)))
        # 7
        for i in range(24):
            if a17[i] > a18[i]:
                raz = a17[i] - a18[i]
                delt = float(raz / 31)
                k = a17[i]
                for j in range(31):
                    k = k - delt
                    a27.append(float("{0:.3f}".format(k)))
            elif a17[i] < a18[i]:
                raz = a18[i] - a17[i]
                delt = float(raz / 31)
                k = a17[i]
                for j in range(31):
                    k = k + delt
                    a27.append(float("{0:.3f}".format(k)))
            elif a17[i] == a18[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 31)
                k = a17[i]
                for j in range(31):
                    k = k + delt
                    a27.append(float("{0:.3f}".format(k)))
        # 8
        for i in range(24):
            if a18[i] > a19[i]:
                raz = a18[i] - a19[i]
                delt = float(raz / 31)
                k = a18[i]
                for j in range(31):
                    k = k - delt
                    a28.append(float("{0:.3f}".format(k)))
            elif a18[i] < a19[i]:
                raz = a19[i] - a18[i]
                delt = float(raz / 31)
                k = a18[i]
                for j in range(31):
                    k = k + delt
                    a28.append(float("{0:.3f}".format(k)))
            elif a18[i] == a19[i]:
                raz = a19[i] - a18[i]
                delt = float(raz / 31)
                k = a18[i]
                for j in range(31):
                    k = k + delt
                    a28.append(float("{0:.3f}".format(k)))
        # 9
        for i in range(24):
            if a19[i] > a110[i]:
                raz = a19[i] - a110[i]
                delt = float(raz / 30)
                k = a19[i]
                for j in range(30):
                    k = k - delt
                    a29.append(float("{0:.3f}".format(k)))
            elif a19[i] < a110[i]:
                raz = a110[i] - a19[i]
                delt = float(raz / 30)
                k = a19[i]
                for j in range(30):
                    k = k + delt
                    a29.append(float("{0:.3f}".format(k)))
            elif a19[i] == a110[i]:
                raz = a110[i] - a19[i]
                delt = float(raz / 30)
                k = a19[i]
                for j in range(30):
                    k = k + delt
                    a29.append(float("{0:.3f}".format(k)))
        # 10
        for i in range(24):
            if a110[i] > a111[i]:
                raz = a110[i] - a111[i]
                delt = float(raz / 31)
                k = a110[i]
                for j in range(31):
                    k = k - delt
                    a210.append(float("{0:.3f}".format(k)))
            elif a110[i] < a111[i]:
                raz = a111[i] - a110[i]
                delt = float(raz / 31)
                k = a110[i]
                for j in range(31):
                    k = k + delt
                    a210.append(float("{0:.3f}".format(k)))
            elif a110[i] == a111[i]:
                raz = a111[i] - a110[i]
                delt = float(raz / 31)
                k = a110[i]
                for j in range(31):
                    k = k + delt
                    a210.append(float("{0:.3f}".format(k)))
        # 11
        for i in range(24):
            if a111[i] > a112[i]:
                raz = a111[i] - a112[i]
                delt = float(raz / 30)
                k = a111[i]
                for j in range(30):
                    k = k - delt
                    a211.append(float("{0:.3f}".format(k)))
            elif a111[i] < a112[i]:
                raz = a112[i] - a111[i]
                delt = float(raz / 30)
                k = a111[i]
                for j in range(30):
                    k = k + delt
                    a211.append(float("{0:.3f}".format(k)))
            elif a111[i] == a112[i]:
                raz = a12[i] - a11[i]
                delt = float(raz / 30)
                k = a111[i]
                for j in range(30):
                    k = k + delt
                    a211.append(float("{0:.3f}".format(k)))
        # 12
        for i in range(24):
            if a112[i] > a11[i]:
                raz = a112[i] - a11[i]
                delt = float(raz / 31)
                k = a112[i]
                for j in range(31):
                    k = k - delt
                    a212.append(float("{0:.3f}".format(k)))
            elif a112[i] < a11[i]:
                raz = a11[i] - a112[i]
                delt = float(raz / 31)
                k = a112[i]
                for j in range(31):
                    k = k + delt
                    a212.append(float("{0:.3f}".format(k)))
            elif a112[i] == a11[i]:
                raz = a11[i] - a112[i]
                delt = float(raz / 31)
                k = a112[i]
                for j in range(31):
                    k = k + delt
                    a212.append(float("{0:.3f}".format(k)))

        begin = []
        for i in range(336):
            begin.append(a212[i])
        end = []
        for i in range(336, 744):
            end.append(a212[i])

        a3 = begin + a21 + a22 + a23 + a24 + a25 + a26 + a27 + a28 + a29 + a210 + a211 + end

        a11.clear()
        a12.clear()
        a13.clear()
        a14.clear()
        a15.clear()
        a16.clear()
        a17.clear()
        a18.clear()
        a19.clear()
        a110.clear()
        a111.clear()
        a112.clear()
        a21.clear()
        a22.clear()
        a23.clear()
        a24.clear()
        a25.clear()
        a26.clear()
        a27.clear()
        a28.clear()
        a29.clear()
        a210.clear()
        a211.clear()
        a212.clear()
        begin.clear()
        end.clear()


        if Period == 'All_period':
        # Шаг дискретизации 1 час
            if Hour == 'Hour_1':

                response = HttpResponse(content_type='text/csv')
                writer = csv.writer(response)
                response['Content-Disposition'] = 'attachment; filename = "sum.csv"'

                writer.writerow([' ', 'HOY', 'DOY', 'Month', 'Day', 'Hour', 'GHI', 'DHI', 'DirectHI', 'Albedo'])

                for i in range(8760):
                    writer.writerow([i, HOY[i], DOY[i], month[i], day[i], hour[i], a1[i], a3[i], a2[i], a[i]])

        # Шаг дискретизации 2 часа
            if Hour == 'Hour_2':

                response = HttpResponse(content_type='text/csv')
                writer = csv.writer(response)
                response['Content-Disposition'] = 'attachment; filename = "sum.csv"'

                writer.writerow([' ', 'HOY', 'DOY', 'Month', 'Day', 'Hour', 'GHI', 'DHI', 'DirectHI', 'Albedo'])

                j = 0
                for i in per:
                    writer.writerow([j, HOY[i], DOY[i], month[i], day[i], hour[i], a1[i], a3[i], a2[i], a[i]])
                    j = j + 1

        # Данные за указанный интервал
        if Period == 'Part_Period':
            Mes_begin = request.GET.get('Mes_begin')
            Day_begin = request.GET.get('Day_begin')
            Hour_begin = request.GET.get('Hour_begin')

            Mes_end = request.GET.get('Mes_end')
            Day_end = request.GET.get('Day_end')
            Hour_end = request.GET.get('Hour_end')

            sum_begin = 0
            sum_end = 0

            for i in range(1, int(Mes_begin)):
                if i in [1, 3, 5, 7, 8, 10, 12]:
                    sum_begin = sum_begin + 744
                if i == 2:
                    sum_begin = sum_begin + 672
                if i in [4, 6, 9, 11]:
                    sum_begin = sum_begin + 720

            sum_begin = sum_begin + int((int(Day_begin) - 1) * 24)
            sum_begin = sum_begin + int(Hour_begin)

            for i in range(1, int(Mes_end)):
                if i in [1, 3, 5, 7, 8, 10, 12]:
                    sum_end = sum_end + 744
                if i == 2:
                    sum_end = sum_end + 672
                if i in [4, 6, 9, 11]:
                    sum_end = sum_end + 720

            sum_end = sum_end + int((int(Day_end) - 1) * 24)
            sum_end = sum_end + int(Hour_end)

            # Шаг дискретизации 1 час
            if Hour == 'Hour_1':

                response = HttpResponse(content_type='text/csv')
                writer = csv.writer(response)
                response['Content-Disposition'] = 'attachment; filename = "sum.csv"'

                writer.writerow([' ', 'HOY', 'DOY', 'Month', 'Day', 'Hour', 'GHI', 'DHI', 'DirectHI', 'Albedo'])
                j = 0
                for i in range(sum_begin - 1, sum_end):
                    writer.writerow([j, HOY[i], DOY[i], month[i], day[i], hour[i], a1[i], a3[i], a2[i], a[i]])
                    j = j + 1

            # Шаг дискретизации 2 часа
            if Hour == 'Hour_2':

                response = HttpResponse(content_type='text/csv')
                writer = csv.writer(response)
                response['Content-Disposition'] = 'attachment; filename = "sum.csv"'

                writer.writerow([' ', 'HOY', 'DOY', 'Month', 'Day', 'Hour', 'GHI', 'DHI', 'DirectHI', 'Albedo'])
                j = 0
                for i in per:
                    if i in range(sum_begin - 1, sum_end + 1):
                        writer.writerow([j, HOY[i], DOY[i], month[i], day[i], hour[i], a1[i], a3[i], a2[i], a[i]])
                        j = j + 1


    return response


    #Period = request.GET.get('Period')
    #Type = request.GET.get('Type')
    #Hour = request.GET.get('Hour')
    #if Period == 'All_period':
                    # h = 1
        #if Type == 'Type_surok':
            #if Hour == 'Hour_1':
                #h = 1
    #elif Period == 'Part_Period':
       # h = 2
    #d=[]
   # d = begin + end
    #leng = len(a212)
   # leng1 = len(a)
    #return render(request, 'MainApp/Ex.html', context={'res1': a, 'b':a21})


