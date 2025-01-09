from .models import List, ListItem
from django.forms import Form, ModelForm
from django.forms import Textarea, CheckboxInput


class ListForm(ModelForm):
    class Meta:
        fields = "__all__"

        widgets = {
            "listItems": Textarea(),
            "ordered": CheckboxInput()
        }