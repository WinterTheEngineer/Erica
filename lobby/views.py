from django.shortcuts import render

# Create your views here.
def lobby(request):

    context = {
        'sector': "Lobby"
    }

    return render(request, 'base.html', context)