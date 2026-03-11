var=input("(B/C): ")
var1=int(input("quantidade: "))
var2=int(input("cappuccinos"))
if(var == "C"):
	valor=(var1*6.00)+(var2*5.50)
else:
	valor=var1*3.00+var2*5.50
print(round(valor,1))
	