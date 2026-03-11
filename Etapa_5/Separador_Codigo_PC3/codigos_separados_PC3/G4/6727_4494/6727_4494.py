num = int(input("Digite um numero inteiro:\n"))

if num % 31 == 0:
	print(num//31)
	msg = "sim"
else:
	print(num%31)
	msg = "nao"

print(msg)