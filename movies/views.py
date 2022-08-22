from django.http import HttpResponse
from django.shortcuts import render

data={
    'movies':[
        {
            'id':5,
            'title':'Jaws',
            'year': '1976'
        },
        {
            'id':6,
            'title':'Terminator',
            'year': '1991'
        },
        {
            'id':7,
            'title':'Megalodon',
            'year': '1999'
        }
    ]
}

def movies(request):
    return render(request, 'movies/movies.html',data )

def home(request):
    return HttpResponse("Home page") 