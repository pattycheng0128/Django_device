from django.shortcuts import render
from .models import TB_1

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        age = request.POST.get('age', None)
        obj = TB_1.objects.create(name=name, age=age)
        obj.save()
        
    user_data = TB_1.objects.get(name="Miya")
    return render(request, 'polls/index.html', {'user_data': user_data})
