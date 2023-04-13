from django import forms
from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):
    # set width of the input spaces
    code = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 8}))
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 15}))
    category = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 15}))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows': 1, 'cols': 30}))
    quantity = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 8}))
    count = forms.FloatField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 8}))
    class Meta:
        model = Item
        fields = ['code','name','category','description','quantity','count']




class CreateNewInventory(forms.Form):
    name = forms.CharField(label="Name", max_length=200)