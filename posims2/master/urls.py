from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("",views.mah_root, name='root'),
    path("home/",views.home, name='home'),
    path("<str:id>",views.index, name='index'),
    path("table_form<int:id>/",views.update, name='update'),
    path("edit_table/<int:lsid>/<int:itid>",views.edit, name='edit'),
]