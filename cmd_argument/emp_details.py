import sys
ename=sys.argv[1]
job=sys.argv[2]
basic_sal=int(sys.argv[3])

print("Employee name is: ",ename)
print("Employee job is: ",job)
print("Employee basic salary is: ",basic_sal)

hra=basic_sal*0.30
print("HRA is: ",hra)

ta=basic_sal*0.20
print("TA is: ",ta)

pf=basic_sal*0.10
print("PF is: ",pf)

Allowances=hra+ta+pf
total_sal=basic_sal+Allowances
annual_sal=total_sal*12

print("Allowances: ",Allowances)
print("Total salary: ",total_sal)
print("Annual salary is: ",annual_sal)

