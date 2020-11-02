import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    #datetime modular
    now = datetime.datetime.now()
    return render(request, 'newyear/index.html', {
        'newyear': now.month == 11 and now.day == 2
    })