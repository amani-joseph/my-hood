from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """
    view to render the index.
    """
    title = 'My-Hood'
    context = {
        'title': title,

    }
    # return render(request, )
    return render(request, 'myhood/index.html')

def about(request):
    return render(request, 'myhood/about.html')
