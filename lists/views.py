from .forms import ListForm
from .models import List, ListItem
from django.shortcuts import render, redirect

# Create your views here.
def lists(request):

    context = {
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
                new_list_item = ListItem(name=list_item)
                new_list_item.save()
                new_list.listItems.add(new_list_item)
            
            # Finally, save the list
            
        else:
            print(form.errors)
    else:
        form = ListForm()
    
    return redirect('lists')