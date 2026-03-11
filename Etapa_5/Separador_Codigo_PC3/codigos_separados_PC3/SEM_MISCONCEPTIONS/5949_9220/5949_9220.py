opcao = input("bolo ou croissant (B/C) ")
var1 = int(input("quantidade de blos ou croissant? "))
var2 = int(input("quantidade de cappuccinos? "))

if (opcao.upper() == "B"):
	total = (var1 * 3) + (var2 * 5.5)
	
else :
	total = (var1 * 6) + (var2 * 5.5)
	
print(round(total,1))
