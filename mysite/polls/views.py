from django.shortcuts import render

# Create your views here.
def index(request):
    args = {
        'name': 'wxy',
        'age': 18,
        'vip': True,
        'dc':{
            'a': 10,
            'b': 20                
        },
        'loops': [1,5,6,9]
    }
    return render(request, 'polls/index.html', args)
