from django.shortcuts import render

# Create your views here.
def lists(request):

    context = {
        'sector': "Lists"
    }

    return render(request, 'lists.html', context)