from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.http.response import StreamingHttpResponse
from django.urls import reverse
import pickle
import os
import schedule
import time
import mysql.connector
import face_recognition
import collections
import cv2
import pytesseract
import datetime
import numpy as np
import imutils
from django.contrib import messages
import datetime
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def process_image(request):
    print("HELLO!!!")
    if request.method == 'POST':
        print(request.POST.get('data', ""))
        # with open("./static/images/temp/1.png", 'w') as f:
        #    f.write(request.POST['image'])

    return HttpResponse("uploaded")


def index(request):
    print("BOBO")
    return render(request, 'index.html')

