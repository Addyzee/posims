from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Inventory,Item
from .forms import ItemForm, InventoryForm
from django.contrib import messages


def edit(response,lsid,itid):
    ls = Inventory.objects.get(id=lsid)
    it = ls.item_set.get(id=itid)
    form = ItemForm(instance=it)
    context = {"ls":ls,"it":it, "form": form}
    if response.method == "POST":
        form = ItemForm(response.POST, instance=it)
        if form.is_valid():
            it = form.save(commit=False)
            it.save()
            return redirect(update,lsid)
        
    return render(response, "master/edit_table.html", context) 

def delete(response,lsid,itid):
    ls = Inventory.objects.get(id=lsid)
    it = ls.item_set.get(id=itid)
    context = {"ls":ls,"it":it}
    if response.method == "POST":
        it.delete()
        return redirect(update,ls.id)
    return render(response,"master/delete.html",context)



# add items to inventory
def update(response,id):
    ls = Inventory.objects.get(id=id)
    form = ItemForm()
    context = {'form':form, "ls":ls}
    if response.method == "POST":
        form = ItemForm(response.POST)
        if form.is_valid():
            it = form.save(commit=False)
            it.inventory_id = id
            it.save()
    return render(response, "master/table_form.html", context) 

def create_inventory(response):
    if response.method=="POST":
        form = InventoryForm(response.POST)

        if form.is_valid():
            inv_name = form.cleaned_data['name']
            ls=response.user.inventory_set.create(name=inv_name)
            ls.save()
        return HttpResponseRedirect("/%i"%ls.id)
    else: 
        ls=response.user.inventory_set.all()
        form = InventoryForm()
    context={"form":form,"ls":ls}
    return render(response,"master/create.html",context)



# Access a certain inverntory using its id
def index (response,id):
    ls = Inventory.objects.get(id=id)
    if ls in response.user.inventory_set.all():
        return render(response, "master/table.html", {"ls":ls}) 
    else: 
        messages.warning(response, "Can't access inventory")
        return redirect("home")

# home page
def home(response):
    ls=response.user.inventory_set.all()
    context = {"ls":ls}
    return render(response, "master/home.html", context) 

def mah_root(response):
    return render(response, "master/home.html", {}) 

