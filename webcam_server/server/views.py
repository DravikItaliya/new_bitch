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
        received_json_data = json.loads(request.POST.get('data'))
        print(received_json_data)
    #     with open(f"{path}{time.strftime('%Y%m%d-%H%M%S')}.png", 'wb') as f:
    #         img_data = request.POST['image']
    #         format, imgstr = img_data.split(';base64,')
    #         f.write(b64decode(imgstr))
    # if len(os.listdir(path)) == 5:
    #     for file in os.listdir(path):
    #         file_path = str(path) + str(file)
    #         # print(file_path)
    #         predictions = predict_pic(file_path)
    #         print(predictions)
    #         adhar = predictions[0][0]
    #         os.remove(file_path)
    #         user_data = retrieve_data(adhar)
    #         user_list.append(user_data)
    #
    #     send_response(user_list)

    return HttpResponse("uploaded")


def retrieve_data(adhar):
    udata = defaultdict()
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
