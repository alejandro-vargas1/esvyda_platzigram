#Platzigram views

#imports Django
from django.http import HttpResponse

#imports libraries
import json

#imports utilities
from datetime import datetime
import pdb

def hello_world(request): 
    return HttpResponse('current server time is: {now}'.format(
        now = datetime.now().strftime('%dth %b, %Y - %H:%M hrs')
    ))


def sorted(request):
    #sorted
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    numbers_sorted = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': numbers_sorted,
        'message': 'Integers sorted succesfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )

def hi(request,name,age):
    #hi
    if age < 12:
        message = 'Sorry {name}, you are not allowed here'.format(name=name)
    else:
        message = 'Welcome to Platzigram {name}'.format(name = name)
    
    return HttpResponse(message)