ent = int(input("numero inteiro: "))

cont = 0 #conta os multiplos de 3
acum = 0 #qtd de numeros digitados

while ent > 0:
	if ent % 3 == 0:
		cont = (cont + 1)
	acum = acum + 1
	ent = int(input("numero inteiro: "))
	
print(acum)
total = 100
acum = total
nao_divisivel = acum - cont * 10
print((100 * cont)/acum )
