from django.shortcuts import render, redirect

from .models import *
from .forms import *

def todo_listaus(request):

    form = TehtavaLomake()

    if request.method == 'POST':
        form = TehtavaLomake(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    todo_list = Tehtava.objects.order_by('id')
    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todos/listaus.html', context)

def yksi_listaus(request, todo_id):

    todo = Tehtava.objects.filter(id=todo_id).get()
    context = {'todo' : todo}

    return render(request, 'todos/yksi_listaus.html', context)