menu = input("T/S:")
qtd = int(input("quantos? "))
acai = int(input("quantos acai? "))

if menu == "T":
	v_total = (qtd*4.50) + (12*acai)
	print(v_total)
	
else:
	v_total2 = (qtd*5) + (12*acai)
	print(v_total2)