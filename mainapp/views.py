from django.shortcuts import render, redirect
from mainapp.forms import DataForm
from mainapp.models import Data
from .export_helper import export_data

def index(request):
    form = DataForm()
    queryset = Data.objects.all()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'title': 'Simple App', 'form': form, 'posts': queryset}
    return render(request, 'mainapp/index.html', context=context)

def export(request):
    export_data()
    return render(request, 'mainapp/export.html')