from django.shortcuts import render, redirect

from .models import *
from .forms import *

#-----------------------------------------------------------------------

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

#--------------------------------------------------------------------------

def yksi_listaus(request, todo_id):

    todo = Tehtava.objects.filter(id=todo_id).get()
    context = {'todo' : todo}

    return render(request, 'todos/yksi_listaus.html', context)

#----------------------------------------------------------------------------------

def paivita_tehtava(request, pk):
    tehtava = Tehtava.objects.get(id=pk)

    form = TehtavaLomake(instance=tehtava)

    if request.method == 'POST':
        form = TehtavaLomake(request.POST, instance=tehtava)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}

    return render(request, 'todos/paivita_tehtava.html', context)

#-------------------------------------------------------------------------------------

def poista_tehtava(request, pk):

    tehtava = Tehtava.objects.get(id=pk)

    if request.method == 'POST':
        tehtava.delete()
        return redirect('/')

    context = {'tehtava' : tehtava}
    return render(request, 'todos/poista_tehtava.html', context)

#--------------------------------------------------------------------------------------