lumsumamt=int(input('Enter lumsum amount :'))
year=int(input('Enter year :'))

print('lumsum amount is :',lumsumamt)
print('you have seleted year :',year)



if year==1 :
   
   intrest=lumsumamt*0.10

   mat_amt=lumsumamt+intrest
   print('intrest amount is', intrest)
   print('maturity amount is', mat_amt)


if year==3 :
   
   intrest=lumsumamt*0.20
   mat_amt=lumsumamt+intrest
   print('intrest amount is' ,intrest)
   print('maturity amount is' ,mat_amt)

if year==5 :
   
   intrest=lumsumamt*0.30
   mat_amt=lumsumamt+intrest
   print('intrest amount is' ,intrest)
   print('maturity amount is' ,mat_amt)



else:
	print('you dnot have any intrest')