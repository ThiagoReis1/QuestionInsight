n = int(input("numero: "))

i = 0   #variavel contadora para numeros dentro do intervalo

while n != -1:
	if 0 <= n <= 25:
		i = i + 1
	n = int(input("numero: "))
print(i)
	