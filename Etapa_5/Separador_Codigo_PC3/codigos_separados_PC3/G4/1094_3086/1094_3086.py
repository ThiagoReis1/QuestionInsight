n = float(input("digite o numero aqui (seis digitos): "))
d1 = n // 1000
resto = n % 1000
if((d1 + resto)**2 != n):
	msg = "nao atende"
else:
	msg = "atende"
print(msg)
print(int(n))



