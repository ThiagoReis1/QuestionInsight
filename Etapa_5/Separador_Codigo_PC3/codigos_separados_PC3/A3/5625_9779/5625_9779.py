tapioca=5.50
salgado=4.00
acai=10.00

T=tapioca
S=salgado

oque=input("O que deseja comprar:")

quantos=int(input("quantos:"))

accai=int(input("acai:"))

if (oque=="T"):
	total=(quantos*5.50)+(accai*10.00)
	print(round(total,2))
	
else:
	total=(quantos*4.00)+(accai*10.00)

	print(round(total,2))