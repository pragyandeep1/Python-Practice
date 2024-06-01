import openpyxl
my_wb = openpyxl.Workbook()
my_sheet = my_wb.active
my_sheet.title = "My New Sheet"
print("Sheet name is: " + my_sheet.title)
