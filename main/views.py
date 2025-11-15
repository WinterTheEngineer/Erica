from django.shortcuts import render

# Create your views here.
def landing(request):

    context = {
        'page_title': 'EricaOS | Lifestyle and Productivity'
    }

    return render(request, 'main/landing.html', context)