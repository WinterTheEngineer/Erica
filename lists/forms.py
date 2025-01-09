from django import forms
from .models import List, ListItem
from django.forms import Textarea, CheckboxInput
from django.utils.translation import gettext_lazy as _


# class ListForm(ModelForm):
#     class Meta:
#         model = List
#         fields = "__all__"

#         widgets = {
#             "listItems": Textarea(),
#             "ordered": CheckboxInput()
#         }

#         labels = {
#             "listItems": _("List Items")
#         }

class ListForm(forms.Form):

    title = forms.CharField(required=True)
    description = forms.CharField(required=False)
    listItems = forms.CharField(widget=Textarea, required=False)
    ordered = forms.BooleanField(widget=CheckboxInput)
