from django.shortcuts import render, redirect
from .models import List
from .forms import ListForms
from django.views.generic import CreateView
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForms(request.POST or None)
        if form.is_valid():
            form.save()
            lists = List.objects.all()
            return render(request, 'Home/index.html', {'lists': lists})

    else:
        lists = List.objects.all()
        return render(request, 'Home/index.html', {'lists': lists})

def edit(request, id):
    if request.method == 'POST':
        item = List.objects.get(pk=id)
        form = ListForms(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        lists = List.objects.get(pk=id)
        return render(request, 'home/edit.html', {'lists': lists})

def delete(request, id):
    list = List.objects.get(pk=id)
    list.delete()
    return redirect('home')


def cross_of(request, id):
    list = List.objects.get(pk=id)
    list.completed = True
    list.save()
    return redirect('home')

def uncross(request, id):
    list = List.objects.get(pk= id)
    list.completed = False
    list.save()
    return redirect('home')


class PostAddView(CreateView):
    model = List
    template_name = 'Home/index.html'
    fields = '__all__'
