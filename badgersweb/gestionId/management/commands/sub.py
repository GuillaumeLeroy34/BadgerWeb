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
            client.subscribe("fx4431@gmail.com/RFID")

        def reponse(valeurReponse):
            client = mqtt.Client()
            client.username_pw_set(username="fx4431@gmail.com",password="badger")
            client.on_connect = on_connect
            client.connect("maqiatto.com", 1883, 60)
            client.publish("fx4431@gmail.com/reponse",valeurReponse)
            t=round(time.time())
            
    # The callback for when the client receives a CONNACK response from the server.
        def on_message(client, userdata, msg):
            print(str(msg.payload))
            rfidPayload=msg.payload.hex()
            try:
                user = User.objects.get(rfid=rfidPayload)
                if user.estAutorise:
                    user.nombrePassage +=1
                    user.save()
                    self.stdout.write(self.style.SUCCESS("Mise à jour réussie"))
                    reponse(1)
                else:
                    self.stdout.write(self.style.WARNING("L'utilisateur n'est pas autorisé à entrer"))
                    reponse(0)
            except User.DoesNotExist:
                self.stdout.write(self.style.ERROR("Utilisateur introuvable avec le rfid:{}".format(rfidPayload)))
                reponse(0)
        
        
        
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