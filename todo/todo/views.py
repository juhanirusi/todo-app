from django.shortcuts import render

from .models import Tehtava

from django.http import HttpResponse

def todo_listaus(request):

    todo_list = Tehtava.objects.order_by('id')
    context = {'todo_list' : todo_list}

    return render(request, 'todos/listaus.html', context)

def yksi_listaus(request):
    return render(request, 'todos/yksi_listaus.html')