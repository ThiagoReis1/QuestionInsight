var1= input("escala (C/K): ")
var2=float(input("valor da temp: "))
if(var1 == "K"):
	conver= var2-273.15
else:
	conver= var2+273.15
print(round(conver,2))