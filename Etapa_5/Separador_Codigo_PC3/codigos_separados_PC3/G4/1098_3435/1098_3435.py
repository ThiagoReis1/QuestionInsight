n = int(input(" Qual o numero de 6 digitos ? :"))

if	(n == ((n // 1000) - (n % 1000))**4 ):
	msg = " atende "

else:
	msg = " nao atende "

print(n)
print(msg)
