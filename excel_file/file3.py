import xlsxwriter

rollno=input("Enter Roll Number: ")
name=input("Enter Student Name: ")
City=input("Enter City: ")
phy=int(input("Enter phy marks: "))
chem=int(input("Enter chem marks: "))
math=int(input("Enter  math's marks: "))

total_marks=phy + chem + math;

percentage=total_marks/3;

workbook=xlsxwriter.Workbook('Student_dataX.xlsx');
test_sheet=workbook.add_worksheet();



test_sheet.write('A1','Rollno');
test_sheet.write('B1','Name');
test_sheet.write('C1','City');
test_sheet.write('D1','Phy');
test_sheet.write('E1','Chem');
test_sheet.write('F1','Math');
test_sheet.write('G1','Total');
test_sheet.write('H1','Percentage');
test_sheet.write('I1','Result');



if(phy>=40 and chem>=40 and math>=40):

 test_sheet.write('A2',rollno);
 test_sheet.write('B2',name);
 test_sheet.write('C2',City);
 test_sheet.write('D2',phy);
 test_sheet.write('E2',chem);
 test_sheet.write('F2',math);
 test_sheet.write('G2',total_marks);
 test_sheet.write('H2',percentage);
 test_sheet.write('I2','Pass');


else:
 test_sheet.write('A2',rollno);
 test_sheet.write('B2',name);
 test_sheet.write('C2',City);
 test_sheet.write('D2',phy);
 test_sheet.write('E2',chem);
 test_sheet.write('F2',math);
 test_sheet.write('G2',total_marks);
 test_sheet.write('H2',percentage);
 test_sheet.write('I2','Fail');


print("Data write in file sucessfylly");

workbook.close();



