import os

from .models import Face
from .prediction import predict_pic
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from pybase64 import b64decode
import time
import json
from django.http import JsonResponse
from collections import defaultdict
import requests

@csrf_exempt
def process_image(request):
    user_list = list()
    path = 'C:/Users/darvik07/Desktop/Server Today/webcam_server/server/static/images/temp/'
    if request.method == 'POST':
        # print(request.POST.getlist('data[]'))
        for i in range(5):
            img_data = request.POST[f'photo{i}']
            # print(img_data)
            format, imgstr = img_data.split(';base64,')
            with open(f"{path}{time.strftime('%Y%m%d-%H%M%S')}'m'{i}.png", 'wb') as f:
                f.write(b64decode(imgstr))
    for f in os.listdir(path):
        file_path = str(path) + str(f)
        predictions = predict_pic(file_path)
        # print(predictions)
        if predictions:
            adhar = predictions[0][0]
            user_data = retrieve_data(adhar)
            user_list.append(user_data)
        os.remove(file_path)

    print(user_list)
    for item in user_list:
        if item['Name'] != 'unknown':
            return HttpResponse(json.dumps(item), content_type="application/json")

    return HttpResponse(json.dumps(user_list[0]), content_type="application/json")


def retrieve_data(adhar):
    udata = defaultdict()
    print(adhar)
    if adhar != 'unknown':
        data = Face.objects.get(adharno=adhar)
        udata['Name'] = data.name
        udata['Rank'] = data.rank
        udata['Number'] = data.number
        udata['Adhar'] = data.adharno
        udata['Cat'] = data.cat
        udata['gender'] = data.gender
        udata['B'] = data.blacklist
        udata['snumber'] = data.snumber
    else:
        udata['Name'] = 'unknown'
        udata['Rank'] = 'unknown'
        udata['Number'] = 'unknown'
        udata['Adhar'] = 'unknown'
        udata['Cat'] = 'unknown'
        udata['gender'] = 'unknown'
        udata['B'] = 'unknown'
        udata['snumber'] = 'unknown'

    return udata


def send_response(data):
    for i in data:
        for k, v in i.items():
            if v != 'unknown':
                return JsonResponse(i)

    return JsonResponse(data[0])

def index(request):
    # print("BOBO")
    return render(request, 'index.html')
