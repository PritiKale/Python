import xlsxwriter

workbook=xlsxwriter.Workbook('student.xlsx');

test_sheet=workbook.add_worksheet();

test_sheet.write('A1','Alex');
test_sheet.write('B1','Jhon');
test_sheet.write('C1','Martin');
test_sheet.write('D1','Ankita');

print("Data write in file sucessfylly");

workbook.close();