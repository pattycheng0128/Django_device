# forms.py
from django import forms
from .models import PhoneDevice

class PhoneDeviceForm(forms.ModelForm):
    class Meta:
        model = PhoneDevice
        fields = ['brand', 'model_name', 'price', 'description']
