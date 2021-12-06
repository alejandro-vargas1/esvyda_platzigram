#post views

#import django
from django.shortcuts import render
from django.http import HttpResponse

#import utilities
from datetime import datetime

posts = [
    {
        'name':'Mont Blanc',
        'user':'yesica cortez',
        'timestamp':datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'pictures':'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name':'Via lactea',
        'user':'C. Vander',
        'timestamp':datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'pictures':'https://picsum.photos/200/200/?image=903'
    }
]

# Create your views here.
def list_posts(request):
    #List existing posts
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{pictures}"></figure>
        """.format(**post))

    return HttpResponse('<br>'.join(content))