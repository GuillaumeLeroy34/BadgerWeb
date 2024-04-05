from django import forms

class UserForm(forms.Form):
    nom = forms.CharField(label='nom', max_length=50)
    prenom = forms.CharField(label='prenom', max_length=50)
    rfid = forms.CharField(label='RFID', max_length=100)
    
 
            