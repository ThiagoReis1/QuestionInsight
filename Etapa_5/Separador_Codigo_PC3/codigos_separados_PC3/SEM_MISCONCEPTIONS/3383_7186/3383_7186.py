unidade= input("Qual a unidade de medida L ou K: ").upper
valor= float(input("Qual o valor da medida: "))

K= valor*2.20462
L= valor/2.20462

if (unidade==L):
	print(round(K, 2))
else:
	print(round(L, 2))