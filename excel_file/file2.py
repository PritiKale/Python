import xlsxwriter

empid=101
ename='Priti Kale'
Wages=300
Wdays=20

pay=Wages*Wdays

workbook=xlsxwriter.Workbook('emp.xlsx');

test_sheet=workbook.add_worksheet();

test_sheet.write('A1','Empid');
test_sheet.write('B1','Ename');
test_sheet.write('C1','Wages');
test_sheet.write('D1','Wdays');
test_sheet.write('E1','Payment');

test_sheet.write('A2',empid);
test_sheet.write('B2',ename);
test_sheet.write('C2',Wages);
test_sheet.write('D2',Wdays);
test_sheet.write('E2',pay);



print("Data write in file sucessfylly");

workbook.close();