dado = int(input('numero sorteado: '))

cont = 1
while dado != 6:
	dado = int(input('leia novamente: '))
	cont = cont+ 1
print(cont)