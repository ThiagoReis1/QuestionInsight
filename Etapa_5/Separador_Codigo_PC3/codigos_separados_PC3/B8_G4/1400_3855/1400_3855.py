tipo_de_ataque = input('Digite constricao ou polen:')
#____________________________
if (tipo_de_ataque == "constricao"):
	r = int(input('Numero de Rodadas Preso:'))
	d1 = int(input('Valor do D1:'))
	d2 = int(input('Valor do D2:'))
	dano = r * (d1 + d2 + 1)
elif (tipo_de_ataque == "polen"):
	r = int(input('Numero de Rodadas Preso:'))
	d1 = int(input('Valor do D1:'))
	d2 = int(input('Valor do D2:'))
	dano = d1*d2
#_____________
print(dano)
