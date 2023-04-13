from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventory,Item
from .forms import CreateNewInventory

# <td><input style="width: 100px" type="text" id="code" placeholder="###" /></td>
# <td><input type="text" id="name" placeholder="Name" /></td>
# <td><input type="text" id="category" placeholder="Category" /></td>
# <td><input type="text" id="description" placeholder="Description" /></td>
# <td><input style="width: 100px" type="text" id="quantity" value="Quantity" placeholder="Quantity" /></td>
# <td><input style="width: 100px" type="number" id="Count" placeholder="Count" /></td>
# <td><button style="widt

def edit(response,lsid,itid):
    ls = Inventory.objects.get(id=lsid)
    it = ls.item_set.get(id=itid)
    # ideal case should check what has been posted, and set the required fields and unrequired as they should be
    return render(response, "master/edit_table.html", {"ls":ls,"it":it}) 

# add items to inventory
def update(response,id):
    # only 1 inventory at the moment, so we pass the inventory objects as 1
    ls = Inventory.objects.get(id=id)

    # ideal case should check what has been posted, and set the required fields and unrequired as they should be
    if response.method == "POST":
        code = response.POST.get('code')
        name = response.POST.get('name')
        category = response.POST.get('category')
        description = response.POST.get('description')
        quantity = response.POST.get('quantity')
        count = response.POST.get('count')
        if len(name)>3 and len(category)>3 and count!=0:
            ls.item_set.create(code=code,name=name,category=category,description=description,quantity=quantity,count=count)
        else:
            print("Error")
    
    return render(response, "master/table_form.html", {"ls":ls}) 

# Access a certain inverntory using its id
def index (response,id):
    ls = Inventory.objects.get(id=id)
    return render(response, "master/table.html", {"ls":ls}) 

# home page
def home(response):
    return render(response, "master/home.html", {}) 

