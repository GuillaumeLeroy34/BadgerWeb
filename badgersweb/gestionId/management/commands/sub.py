import paho.mqtt.client as mqtt
import datetime
from datetime import datetime as dt
import time
from time import sleep
from django.core.management.base import BaseCommand
from gestionId.models import User

            
class Command(BaseCommand):


    # The callback for when a PUBLISH message is received from the server.
    def handle(self, *args, **options):
        
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
            client.subscribe("fx4431@gmail.com/badger")

        def reponse(valeurReponse):
            client = mqtt.Client()
            client.username_pw_set(username="fx4431@gmail.com",password="badger")
            client.on_connect = on_connect
            client.connect("maqiatto.com", 1883, 60)
            client.publish("fx4431@gmail.com/reponse",valeurReponse)
            t=round(time.time())
            
    # The callback for when the client receives a CONNACK response from the server.
        def on_message(client, userdata, msg):
            global Whitelist
            global t
            print(str(msg.payload.hex()))
            id=msg.payload.hex()
            tprime=round(time.time())
            if (tprime-t>1):
                try:
                    user = User.objects.get(rfid=id)
                    user.nombrePassage +=1
                    user.save()
                    self.stdout.write(self.style.SUCCESS("Mise à jour réussie"))
                except User.DoesNotExist:
                    self.stdout.write(self.style.ERROR("Utilisateur introuvable avec le rfid:{}".format(id)))
        
        
        
        client = mqtt.Client()
        client.username_pw_set(username="fx4431@gmail.com",password="badger")
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("maqiatto.com", 1883, 60)
        self.stdout.write(self.style.SUCCESS("connexion réussie"))
        client.loop_forever()
        

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.