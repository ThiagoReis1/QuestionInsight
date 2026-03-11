nome = input("Nome da cabeca que atacara?(Aameul/Hethradiah) ")
d1 = int(input("Valor D1: "))
d2 = int(input("Valor D2: "))
d3 = int(input("Valor D3: "))

if("nome" == "Aameul"):
	a = (d1*8)+(d2*3)+(d3*30)
	print(a)
else:
	dano = (d1+d2+d3)*2
	print(dano)
	