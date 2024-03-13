from django.shortcuts import render, redirect, get_object_or_404
from .models import PhoneDevice
from .forms import PhoneDeviceForm

# Create your views here.
def index(request):
    phones = PhoneDevice.objects.all()
    return render(request, 'phone_manager/index.html', {'phones': phones})

def phone_list(request):
    phones = PhoneDevice.objects.all()
    return render(request, 'phone_manager/phone_list.html', {'phones': phones})

def phone_create(request):
    if request.method == 'POST':
        form = PhoneDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PhoneDeviceForm()
    return render(request, 'phone_manager/phone_form.html', {'form': form})

def phone_update(request, pk):
    phone = get_object_or_404(PhoneDevice, pk=pk)
    if request.method == 'POST':
        form = PhoneDeviceForm(request.POST, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PhoneDeviceForm(instance=phone)
    return render(request, 'phone_manager/phone_form.html', {'form': form})

def phone_delete(request, pk):
    phone = get_object_or_404(PhoneDevice, pk=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('index')
    return render(request, 'phone_manager/phone_delete.html', {'phone': phone})

