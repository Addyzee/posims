from django import forms

class CreateNewInventory(forms.Form):
    name = forms.CharField(label="Name", max_length=200)