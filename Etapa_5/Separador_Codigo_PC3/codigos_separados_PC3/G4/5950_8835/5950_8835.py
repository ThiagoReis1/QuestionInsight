ti = input("T ou P:")
qtd=float(input("Quantidade de torta ou pastel:"))
qc=float(input("Quantidade de cappuccinos"))
if (ti) == "T":
	cal =qtd*6 + qc*4.50
else:
	cal =qtd*5 + qc*4.50
print(cal)