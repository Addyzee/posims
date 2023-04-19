from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("",views.mah_root, name='root'),
    path("home/",views.home, name='home'),
    path("create/",views.create_inventory, name='create'),
    path("<int:id>",views.index, name='index'),
    path("table_form/<int:id>/",views.update, name='update'),
    path("edit_table/<int:lsid>/<int:itid>",views.edit, name='edit'),
    path("delete/<int:lsid>/<int:itid>",views.delete, name='delete'),
]