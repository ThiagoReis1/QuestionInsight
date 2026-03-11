ts = input("digite T ou S : ")
qntts = int(input("quantidade de T ou S: "))
qntacai = int(input("digite a quantidade de acai: "))
if ts == 'T' :
	valor = qntts * 4.50 + qntacai * 12.0
	valortotal = float(valor)
	print(round(valortotal , 1))

else :
	valor1 = qntts * 5.0 + qntacai * 12.0
	valortotal1 = float(valor1)
	print(round(valortotal1 ,1))