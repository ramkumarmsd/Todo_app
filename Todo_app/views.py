from django.shortcuts import render,redirect
from .models import todo
from .form import todoform
import datetime
from django.contrib import messages

# Create your views here.
    
def home(request):
    items = todo.objects.order_by("-time")
    
    form = todoform()
    if request.method == "POST":
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    page ={
        'datas':items,
        'form':form,

    }        
    return render(request,'todo.html',page)             


def deldt(request,itemid):
    data = todo.objects.get(id=itemid)
    data.delete()
    messages.success(request,"your task removed successfully...!!!")
    return redirect('home')

def edit(request,itemid):
    data = todo.objects.get(id=itemid)
    form = todoform(instance=data)
    if request.method == "POST":
        form = todoform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')

    page ={
        'form':form,   
    }        
    return render(request,'edit.html',page)  