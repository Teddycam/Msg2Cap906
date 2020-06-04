import openpyxl
book = openpyxl.load_workbook('sample.xlsx')

print('Sheets: ', book.sheetnames)

# assert "Capabilitie" in book.sheetnames, 'Вкладка Capabilities в таблице не найдена'

# try:
#     sheet = book["Capabilitie"]
# except:
#     e = 'Вкладка Capabilities в таблице не найдена'
#     raise ValueError(e)

if "Capabilities" in book.sheetnames:
    # Меняем вкладку
    sheet = book["Capabilities"]
else:
    print('Вкладка Capabilities в таблице не найдена')
    exit(0)
print('Title = ', sheet.title)
s = []
row: object
for row in sheet.iter_rows():
    s.append([cell.value for cell in row])
print(s[-3:])
print ('s length = ', len(s))

# Add new sheet, fill it and save book copy with new sheet
if "Parsed_Cap.Info" not in book.sheetnames:
    ws1 = book.create_sheet("Parsed_Capabilities")                   # insert sheet at the end (by default)
    sheet = book["Parsed_Capabilities"]
    sheet.sheet_properties.tabColor = "1072BA"
    sheet['A1'] = 56
    sheet['A2'] = 43
    sheet['A3'] = 'Test'
    print('Вкладка Cap.Info создана и заполнена')
    book.save("Copy.xlsx")
    print('Копия файла сохранена')
else:
    print('Вкладка Cap.Info уже существует')

print('Конец работы')
exit (0)