from django.shortcuts import render
from django.http import HttpResponse

import paho.mqtt.client as mqtt
import datetime
from datetime import datetime as dt
import time
from time import sleep


from django.http import HttpResponseRedirect
from .forms import UserForm

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def reponse(valeurReponse):
    client = mqtt.Client()
    client.username_pw_set(username="fx4431@gmail.com",password="badger")
    client.on_connect = on_connect
    client.connect("maqiatto.com", 1883, 60)
    client.publish("fx4431@gmail.com/reponse",valeurReponse)

def on_message(client, userdata, msg):
    global Whitelist
    global t
    print(str(msg.payload.hex()))
    id=msg.payload.hex()
    tprime=round(time.time())
    if (tprime-t>1):
        if (id in Whitelist):
            reponse(1)
            t=round(time.time())
        else:
            reponse(0)
            t=round(time.time())

def test(request):
    context = {}
    return render(request, "gestionId/index.html", context)

def gestionId(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        client = mqtt.Client()
        client.username_pw_set(username="fx4431@gmail.com",password="badger")
        client.on_connect = on_connect
        client.connect("maqiatto.com", 1883, 60)
        client.loop_forever()
        client.publish('fx4431@gmail.com/testSite',form.nom)
        # redirect to a new URL:
        return HttpResponseRedirect("/ligma/")

    else:
        form = UserForm()
    return render(request,"gestionID/gererId.html",{'form': form})

    

def gestionIdRequete(request):
        form = UserForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data["prenom"]
            rfid = form.cleaned_data["rfid"]
        client = mqtt.Client()
        client.username_pw_set(username="fx4431@gmail.com",password="badger")
        client.on_connect = on_connect
        client.connect("maqiatto.com", 1883, 60)
        client.publish('fx4431@gmail.com/testSite',(str(nom)))
        return HttpResponseRedirect("/gererId")