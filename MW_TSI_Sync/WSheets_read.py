import xlrd
import os
import kivy
from kivy.app import App
from kivy.uix.button import Label

json_dir_wsheet = 'data/WSheets/WSheets_2018'

cwd = os.getcwd()
dir_WSheets = os.path.join(cwd,json_dir_wsheet)

os.chdir(dir_WSheets)

xls_files = os.listdir()

book = xlrd.open_workbook(xls_files[0])
sheet = book.sheet_by_index(0)

# for i in range(14,49):
#     cell = sheet.cell(i,3)
#     if(cell.ctype==xlrd.XL_CELL_TEXT)==True:
#         text = ""
#         for col in range(2,9):
#             text += str(sheet.cell(i,col).value)
#             text += " "
#         print(i)
#         if (i+1)%5==0:
#             print(xlrd.xldate_as_tuple(sheet.cell(i,0).value,book.datemode))
#         print(text)

print(sheet.nrows)
print(sheet.ncols)
