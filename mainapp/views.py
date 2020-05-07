from django.shortcuts import render, redirect
from mainapp.forms import DataForm
from mainapp import models

def index(request):
    form = DataForm()
    queryset = models.Data.objects.all()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'title': 'Simple App', 'form': form, 'posts': queryset}
    return render(request, 'mainapp/index.html', context=context)


import xlwings as xl
from django.http import HttpResponse
from django.http import FileResponse
import io

def export_data(request):
    #response = HttpResponse(content_type='application/vnd.ms-excel')
    #response['Content-Disposition'] = 'attachment; filename="Data.xlsx"'

    # create workbook
    wb = xl.Book()
    sheet = wb.sheets[0]

    # stylize header row
    # 'id','title', 'quantity','pub_date'
      
    sheet.range('A1').value = 'id'
    sheet.range('A1').api.Font.Bold = True
    
    sheet.range('B1').value = 'title'
    sheet.range('B1').api.Font.Bold = True

    sheet.range('C1').value = 'quantity'
    sheet.range('C1').api.Font.Bold = True

    sheet.range('D1').value = 'pub_date'
    sheet.range('D1').api.Font.Bold = True
    
    # export data to Excel
    rows = models.Data.objects.all().values_list('id','category', 'quantity','pub_date',)
    for row_num, row in enumerate(rows, 2):
        # row is just a tuple
        x = ('A', 'B', 'C', 'D')
        for loc, value in zip(x, row):
            loc = loc + str(row_num)
            sheet.range(loc).value = value

    wb.save("tmp/Data.xlsx")
    wb.close()
    buffer = open("tmp/Data.xlsx", 'rb')
    return FileResponse(buffer, as_attachment=True, filename='Data.xlsx')