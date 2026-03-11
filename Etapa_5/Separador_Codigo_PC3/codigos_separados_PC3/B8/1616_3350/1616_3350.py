from numpy import*
magia = array(eval(input("MAGIA")))
nivel = array(eval(input("NIVEL")))
i = 0

while i < size(magia):
	if (magia[i]) == "GELO":
		dano_da_magia = 2
	elif (magia[i]) == "FOGO":
		dano_da_magia = 3
	elif (magia[i]) == "CHOQUE":
		dano_da_magia = 4
	elif (magia[i]) == "CONJURACAO":
		dano_da_magia = 8
	elif (magia[i]) == "ILUSAO":
		dano_da_magia = 10
	
	dt  = dano_da_magia * float(nivel[i])

print(dt)