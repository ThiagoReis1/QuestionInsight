t_ataque = input("Digite aqui o tipo de ataque: constricao / polen ")
n_rodadas = int(input("Digite aqui o numero de rodadas:"))
valore_1 = int(input("Digite aqui o valor sorteado 1:"))
valore_2 = int(input("Digite aqui o valor sorteado 2:"))

if (t_ataque == "constricao"):
	c = ((valore_1 + valore_2) +1)* n_rodadas
	
else:
	c = valore_1 * valore_2
	
print(c)