c = float(input("Valor da casa: "))
d = float(input("Valor inicial depositado: "))
m = float(input("Deposito mensal fixo: "))
j = float(input("Taxa de juros: "))

t = 0
s = d
if((c>0) and (d>0) and (m>0) and (j>0)):
   while(s < c):
	   s = s + s * j/100 + m
	   s = round(s, 2)
	   t = t + 1
   print(round(t, 2))	
else:
	print("Dados incorretos")