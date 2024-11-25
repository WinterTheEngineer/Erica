from django.shortcuts import render

# Create your views here.
def lobby(request):

    context = {
        'page_title': "Lobby"
    }

    return render(request, 'base.html', context)