from django.shortcuts import render

# Create your views here.
def lobby(request):

    context = {
        'sector': "Lobby"
    }

    if request.htmx:
        return render(request, "partials/lobby_partial.html", context)

    return render(request, 'base.html', context)