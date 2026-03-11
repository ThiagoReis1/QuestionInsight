var1=input("tapioca ou salgado (T/S): ")
var2=int(input("quantidade: "))
var3=int(input("quantidade de acai: "))
tap=4.50
sal=5.00
acai=12.00
if(var1 == "T"):
	cal=(var2*tap)+(var3*acai)
else:
	cal=(var2*sal)+(var3*acai)
print(round(cal,1))