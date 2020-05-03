import xlwings as xl
from mainapp import models
import pythoncom

def export_data():
    pythoncom.CoInitialize()
    app = xl.App()
    wb = app.books[0]
    sheet = wb.sheets[0]
    queryset = models.Data.objects.all()
    for i, query in enumerate(queryset, 1):
        # id
        cell = "a{}".format(i)
        sheet.range(cell).value = query.id
        # title
        cell = "b{}".format(i)
        sheet.range(cell).value = query.title
        # quantity
        cell = "c{}".format(i)
        sheet.range(cell).value = query.quantity
        # pub_data
        cell = "d{}".format(i)
        sheet.range(cell).value = query.pub_date
    wb.save(r"C:\Users\testuser\Desktop\output\output.xlsx")
    wb.close()
    app.quit()
    return 0