var1 = input("bolo ou salgado: (B/S)")
var2 = float(input("Quantidade: "))
var3 = float(input("Quantidade de cappuccinos: "))

bolo = 5.00
salgado = 4.00
cap = 7.50
 
if(var1=="B"):
	total = bolo*var2+cap*var3
	print(round(total, 2))

else:
	total = salgado*var2+cap*var3
	print(round(total, 2))