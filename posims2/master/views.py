from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Inventory,Item
from .forms import ItemForm


def edit(response,lsid,itid):
    ls = Inventory.objects.get(id=lsid)
    it = ls.item_set.get(id=itid)
    form = ItemForm(instance=it)
    context = {"ls":ls,"it":it, "form": form}
    # ideal case should check what has been posted, and set the required fields and unrequired as they should be
    if response.method == "POST":
        form = ItemForm(response.POST, instance=it)
        if form.is_valid():
            it = form.save(commit=False)
            # it.inventory_id = lsid
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
    # only 1 inventory at the moment, so we pass the inventory objects as 1
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

# Access a certain inverntory using its id
def index (response,id):
    ls = Inventory.objects.get(id=id)
    return render(response, "master/table.html", {"ls":ls}) 

# home page
def home(response):
    return render(response, "master/home.html", {}) 

def mah_root(response):
    return render(response, "master/home.html", {}) 

  # ideal case should check what has been posted, and set the required fields and unrequired as they should be
    # if response.method == "POST":
    #     code = response.POST.get('code')
    #     name = response.POST.get('name')
    #     category = response.POST.get('category')
    #     description = response.POST.get('description')
    #     quantity = response.POST.get('quantity')
    #     count = response.POST.get('count')
    #     if len(name)>3 and len(category)>3 and count!=0:
    #         ls.item_set.create(code=code,name=name,category=category,description=description,quantity=quantity,count=count)
    #     else:
    #         print("Error")