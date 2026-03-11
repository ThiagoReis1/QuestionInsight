a = input("L ou K: ")
b = float(input("Digite o valor da medida: "))

if(a == "L"):
	k = b/2.20462
else:
	k = b*2.20462
	
print(round(k,2))