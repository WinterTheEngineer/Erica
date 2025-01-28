from .forms import ListForm
from .models import List, ListItem
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def lists(request):

    lists = List.objects.all

    context = {
        'lists': lists,
        'sector': "Lists",
        'listform': ListForm
    }

    return render(request, 'lists.html', context)


def new_list(request):

    if request.method == "POST":
        form = ListForm(request.POST)

        if form.is_valid():
            # Create List object first
            new_list = List(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                ordered=form.cleaned_data["ordered"]
            )
            new_list.save()

            list_items = form.cleaned_data["listItems"].split(", ")

            for list_item in list_items:
                new_list_item = ListItem(name=list_item, list=new_list)
                new_list_item.save()           
            
        else:
            messages.error(request, "A form validation error prevented me from created the list.")
    else:
        form = ListForm()
    
    messages.success(request, "The list was created successfully.")
    return redirect('lists')