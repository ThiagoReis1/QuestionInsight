x = float(input("Insira o deposito inicial: "))
y = int(input("Insira a qtd de meses: "))

a = 1/100
cont = 1
 
b =(x * a) + x
print(round(b,2))

while(cont < y):
	b = b + (b * a)
	cont += 1
	print(round(b,2))