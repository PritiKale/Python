import xlsxwriter

workbook=xlsxwriter.workbook('anvistar.xlsx');

test_sheet.write('A1','Rollno');
test_sheet.write('B1','Name');
test_sheet.write('C1','City');
test_sheet.write('D1','Phy');
test_sheet.write('E1','Chem');
test_sheet.write('F1','Math');
test_sheet.write('G1','Total');
test_sheet.write('H1','Percentage');
test_sheet.write('I1','Result');

rollno=input("Enter Roll Number: ")
name=input("Enter Student Name: ")
City=input("Enter City: ")
phy=int(input("Enter phy marks: "))
chem=int(input("Enter chem marks: "))
math=int(input("Enter  math's marks: "))

total_marks=phy + chem + math;

percentage=total_marks/3;


test_sheet=workbook.active;

if(phy>=40 and chem>=40 and math>=40):

 test_sheet.append('A2',rollno);
 test_sheet.append('B2',name);
 test_sheet.append('C2',City);
 test_sheet.append('D2',phy);
 test_sheet.append('E2',chem);
 test_sheet.append('F2',math);
 test_sheet.append('G2',total_marks);
 test_sheet.append('H2',percentage);
 test_sheet.append('I2','Pass');


else:
 test_sheet.append('A2',rollno);
 test_sheet.append('B2',name);
 test_sheet.append('C2',City);
 test_sheet.append('D2',phy);
 test_sheet.append('E2',chem);
 test_sheet.append('F2',math);
 test_sheet.append('G2',total_marks);
 test_sheet.append('H2',percentage);
 test_sheet.append('I2','Fail');


print("Data write in file sucessfylly");

workbook.close();



