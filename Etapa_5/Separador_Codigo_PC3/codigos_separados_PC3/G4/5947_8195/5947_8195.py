var = input("(C/E): ")
var1 = int(input("quantidade: "))
var2 = int(input("sucos: "))
if(var == "C"):
	valor = (var1*2.00) + (var2*6.00)
else:
	valor = var1*4.50 + var2*6.00
print(round(valor,1))