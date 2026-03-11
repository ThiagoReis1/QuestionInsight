x = int(input("digite um numero x: "))
y = int(input("digite um numero y: "))
numero = 0

while (x < y) :
	if x % 7 == 0 and y % 7 == 0 :
		numero = numero + 1
print(numero)