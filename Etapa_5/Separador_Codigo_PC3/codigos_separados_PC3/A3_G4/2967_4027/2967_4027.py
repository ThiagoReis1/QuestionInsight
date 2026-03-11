var1=float(input("A sua altura: "))
var2=float(input("A altura do seu amigo: "))
if(var1 > var2):
	MA=var1
	if(var1 > 1.37):
		print("Sim")
	else:
		print("Nao")
if(var2 > var1):
	MA=var2
	if(var2 > 1.37):
		print("Sim")
	else:
		print("Nao")
print(MA)