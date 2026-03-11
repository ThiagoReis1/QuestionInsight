deposito_inicial=float(input("digite seu deposito= "))
meses_depositados=int(input("digite os meses depositados= "))

cont= 0

while meses_depositados >= 0:
	deposito_inicial= deposito_inicial + (meses_depositados * 0.01)
	cont = cont + 1
print(round(deposito_inicial,2))