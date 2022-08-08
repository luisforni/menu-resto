from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class MenuListView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'menu_list.html', context)