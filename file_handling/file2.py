home=open("home.txt","r")
company=open("company.txt","r")


for data in home:
 print("Home Address: ",data)

print("--------------------------------------------------------------------------------")


print(company.read())
print("--------------------------------------------------------------------------------")

# print(company.read(4))

