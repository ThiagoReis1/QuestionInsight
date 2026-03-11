numcopias = int(input("digite o numero de copias no sangue"))
taxareducao = float(input("digite a taxa de reducao de virus"))
copiasintro = int(input("digite o numero de copias introduzidas"))
acum = copiasintro
cont = 0
while(numcopias < 1000000):
	acum = acum + copiasintro
	reducao = (acum * taxareducao)/100
	acum = acum - reducao
	numcopias = numcopias + acum
	cont = cont +1
	print(acum)
	print(numcopias)
print(cont)
