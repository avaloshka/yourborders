from django.shortcuts import render
from .models import Borders
from .belarus import get_border_info
import time
import requests
from datetime import datetime, timedelta
from .poland import get_polish_data
from .models import Polish, Feedback



# CHECK IF AN HOUR HAS PASSED 

# oldtime = time.time()
# def hourPassed(oldtime):
#     currenttime = time.time()
#     if currenttime - oldtime >= 60*60:
#          # and ran == False
#         # ran = True
#         oldtime = currenttime
#         return True
#     else:
#         return False


# if hourPassed:
#     get_border_info()

# get_border_info()


# PARSE THE QUEUES
# def parse_the_queue(querystring):
#     url = "https://belarusborder.by/info/monitoring"
#     payload = ""
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
#         "Accept": "application/json, text/plain, */*",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Origin": "https://mon.declarant.by",
#         "Connection": "keep-alive",
#         "Referer": "https://mon.declarant.by/",
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "cross-site",
#         "Sec-GPC": "1"}
#     response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

#     return response.json()

        # page querystring:
    #querystring = {"checkpointId":"ffe81c11-00d6-11e8-a967-b0dd44bde851",
     #               "token":"bts47d5f-6420-4f74-8f78-42e8e4370cc4"}

def home(request):
    return render(request, 'home.html', {})


# Create your views here.
def belarus_poland(request):
    # Should work if requests are not exceeded the limit
    try:
        # Check if db is younger than 1 hour
        now = datetime.now()
        time_threshold = now - timedelta(hours=1)
        result = Borders.objects.filter(created__range=(time_threshold, now))
        if result: # IF RESULT- DB IS YOUNGER THAN 1 HOUR
            table = Borders.objects.all()
            # message = 'This db is younger than 1 hour'
            return render(request, 'belarus_poland.html', {'table': table})
        else:
            # db is older than 1 hour- get info
            get_border_info()
            table = Borders.objects.all()
            return render(request, 'belarus_poland.html', {'table': table})
    # Over limit- and the page could not be rendered- than-
    except:
        message = 'Публичный лимит исчерпан. Нужно выждать время'
        return render(request, 'belarus_poland.html', {'message': message}) 

def grigorov(request):
    obj = Borders.objects.get(location='Григоровщина')
    return render(request, 'grigorov.html', {'obj': obj,
                                            
                                            })

def urbany(request):
    obj = Borders.objects.get(location='Урбаны')
    return render(request, 'urbany.html', {'obj': obj})


def vidzy(request):
    obj = Borders.objects.get(location='Видзы')
    return render(request, 'vidzy.html', {'obj': obj})

def kotlovka(request):
    obj = Borders.objects.get(location='Котловка')
    return render(request, 'kotlovka.html', {'obj': obj})

def losha(request):
    obj = Borders.objects.get(location='Лоша')
    return render(request, 'losha.html', {'obj': obj})

def kamenny_log(request):
    obj = Borders.objects.get(location='Каменный Лог')
    return render(request, 'kamenny_log.html', {'obj': obj})

def beniakoni(request):
    obj = Borders.objects.get(location='Бенякони')
    return render(request, 'beniakoni.html', {'obj': obj})

def privalka(request):
    obj = Borders.objects.get(location='Привалка')
    return render(request, 'privalka.html', {'obj': obj})

def bruzgi(request):
    obj = Borders.objects.get(location='Брузги')
    return render(request, 'bruzgi.html', {'obj': obj})

def berestovitsa(request):
    obj = Borders.objects.get(location='Берестовица')
    return render(request, 'berestovitsa.html', {'obj': obj})

def peschatka(request):
    obj = Borders.objects.get(location='Песчатка')
    return render(request, 'peschatka.html', {'obj': obj})

def kozlovichi(request):
    obj = Borders.objects.get(location='Козловичи')
    return render(request, 'kozlovichi.html', {'obj': obj})

def brest(request):
    obj = Borders.objects.get(location='Брест')
    return render(request, 'brest.html', {'obj': obj})

def domachevo(request):
    obj = Borders.objects.get(location='Домачево')
    return render(request, 'domachevo.html', {'obj': obj})

def tomashovka(request):
    obj = Borders.objects.get(location='Томашовка')
    return render(request, 'tomashovka.html', {'obj': obj})

def oltush(request):
    obj = Borders.objects.get(location='Олтуш')
    return render(request, 'oltush.html', {'obj': obj})


def mokrany(request):
    obj = Borders.objects.get(location='Мокраны')
    return render(request, 'mokrany.html', {'obj': obj})

def mohro(request):
    obj = Borders.objects.get(location='Мохро')
    return render(request, 'mohro.html', {'obj': obj})

def nevel(request):
    obj = Borders.objects.get(location='Невель')
    return render(request, 'nevel.html', {'obj': obj})

def verhni_terebezhev(request):
    obj = Borders.objects.get(location='Верхний Теребежов')
    return render(request, 'verhni_terebezhev.html', {'obj': obj})

def glushkevichi(request):
    obj = Borders.objects.get(location='Глушкевичи')
    return render(request, 'glushkevichi.html', {'obj': obj})

def novaya_rudnya(request):
    obj = Borders.objects.get(location='Новая Рудня')
    return render(request, 'novaya_rudnya.html', {'obj': obj})

def aleksandrovka(request):
    obj = Borders.objects.get(location='Александровка')
    return render(request, 'aleksandrovka.html', {'obj': obj})

def komarin(request):
    obj = Borders.objects.get(location='Комарин')
    return render(request, 'komarin.html', {'obj': obj})

def novaya_guta(request):
    obj = Borders.objects.get(location='Новая Гута')
    return render(request, 'novaya_guta.html', {'obj': obj})

def veselovka(request):
    obj = Borders.objects.get(location='Веселовка')
    return render(request, 'veselovka.html', {'obj': obj})

def uznat_svou_ochered(request):
    if request.method == 'POST':
        # Try to get info from corresponding location
        try:
            reg = request.POST['reg']

            location_id = request.POST['location_id']

            location_url = f'https://belarusborder.by/info/monitoring?checkpointId={location_id}&token=bts47d5f-6420-4f74-8f78-42e8e4370cc4'
            r = requests.get(location_url)
            data = r.json()

            info = data['info']
            truckBooking = data['truckBooking']
            truckLiveQueue = data['truckLiveQueue']
            truckGpk = data['truckGpk']
            busBooking = data['busBooking']
            busLiveQueue = data['busLiveQueue']
            carBooking = data['carBooking']
            carLiveQueue = data['carLiveQueue']

            

            list_dictionaries = [truckBooking, truckLiveQueue, truckGpk, busBooking, busLiveQueue, carBooking, carLiveQueue]
            for que in list_dictionaries:
                for item in que:
                    if reg in item.values():
                        item = item
                        nomer = item['order_id']
                        if nomer == False:
                            nomer = '-'
                        regnum = item['regnum']
                        status = item['status']
                        if status == 2:
                            status = 'Прибыл в зал ожидания'
                        elif status == 3:
                            status = 'Вызван в пункт пропуска'
                        elif status == 9:
                            status = 'Анулирован'
                        type_queue = item['type_queue']
                        if type_queue == 2:
                            type_queue = 'Платная очередь'
                        elif type_queue == 3:
                            type_queue = 'Живая очередь'
                        registration_date = item['registration_date']
                        changed_date = item['changed_date']
                        location = info['name']
                        address = info['address']
                        phone = info['phone']
                        return render(request, 'uznat_svou_ochered.html', {'item': item,
                                                                            'nomer': nomer,
                                                                            'regnum': regnum,
                                                                            'status': status,
                                                                            'type_queue': type_queue,
                                                                            'registration_date': registration_date,
                                                                            'changed_date': changed_date,
                                                                            'location_id': location_id,
                                                                            'location': location,
                                                                            'address': address, 
                                                                            'phone': phone})
                    
                    message = 'Этого регистрационного номера нет в данном пропускном пункте. Попробуйте в другом или убедитесь, что вы вводите данные правильно'
                    return render(request, 'uznat_svou_ochered.html', {'message': message})

        except:
            message = 'Что-то пошло не так... Я не могу найти информацию о пропускном пункте'
            return render(request, 'uznat_svou_ochered.html', {'message': message})
                

    request_ids_url = 'https://belarusborder.by/info/checkpoint?token=bts47d5f-6420-4f74-8f78-42e8e4370cc4'
    r = requests.get(request_ids_url)
    list_all_locations = r.json()['result']
    return render(request, 'uznat_svou_ochered.html', {'list_all_locations': list_all_locations})

def error(request):
    message = '----'
    return render(request, 'error.html', {'message': message})

def poland(request):
    # Should work if requests are not exceeded the limit
    try:
        # Check if db is younger than 1 hour
        now = datetime.now()
        time_threshold = now - timedelta(hours=1)
        result = Polish.objects.filter(created__range=(time_threshold, now))
        if result: # IF RESULT- DB IS YOUNGER THAN 1 HOUR
            table = Polish.objects.all()
            # message = 'This db is younger than 1 hour'
            return render(request, 'poland.html', {'table': table})
        else:
            # db is older than 1 hour- get info
            get_polish_data()
            table = Polish.objects.all()
            return render(request, 'poland.html', {'table': table})
    # Over limit- and the page could not be rendered- than-
    except:
        message = 'Публичный лимит исчерпан. Нужно выждать время'
        return render(request, 'poland.html', {'message': message})

def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        x = Feedback(name=name,
                    email=email,
                    message=message)
        x.save()


        return render(request, 'feedback.html', {'name': name})
    return render(request, 'feedback.html', {})