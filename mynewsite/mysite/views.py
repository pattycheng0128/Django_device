from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import PhoneDevice
from .forms import PhoneDeviceForm
from django.http import HttpResponse
import csv

# Create your views here.
def index(request):
    phones = PhoneDevice.objects.all()
    # 如果有提交搜尋表單
    if 'search' in request.GET:
        search_term = request.GET['search']
        phones = PhoneDevice.objects.filter(brand__icontains=search_term)

    return render(request, 'phone_manager/index.html', {'phones': phones})

#  ==== 註冊相關功能 ====
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 检查用户名是否已经存在
        if User.objects.filter(username=username).exists():
            return render(request, 'member/register.html', {'error': 'Username already exists'})
        # 创建新用户
        user = User.objects.create_user(username=username, password=password)
        # 登录用户
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'member/register.html')

#  ==== 手機相關功能 ====

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

#  ==== csv功能 ====
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="phone_devices.csv"'

    phones = PhoneDevice.objects.all()

    writer = csv.writer(response)
    writer.writerow(['Brand', 'Model', 'Price', 'Description'])

    for phone in phones:
        writer.writerow([
            phone.brand,
            phone.model_name,
            phone.price,
            phone.description
        ])

    return response

