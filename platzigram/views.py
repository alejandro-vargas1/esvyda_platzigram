#Platzigram views

#imports Django
from django.http import HttpResponse

#imports utilities
from datetime import datetime
import pdb

def hello_world(request): 
    return HttpResponse('current server time is: {now}'.format(
        now = datetime.now().strftime('%dth %b, %Y - %H:%M hrs')
    ))


def hi(request):
    #hi
    pdb.set_trace()
    return HttpResponse('Hi')
