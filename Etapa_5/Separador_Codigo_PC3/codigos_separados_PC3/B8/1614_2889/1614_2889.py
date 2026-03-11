from numpy import* 

nomes = array(eval (input ()))
quantidade = array (eval(input()))

qtd = size(nomes)
#contadora#
cont = 0 
#acumuladora#
banana = 0 
bife = 0
feijoada = 0
omelete = 0
tomate = 0

while (cont < qtd):
	if (nomes[cont] == "BANANA"):
		banana = banana + 0.97 * quantidade[cont]
	elif (nomes[cont] == "BIFE"):
		bife = bife + 2.95 * quantidade[cont]
	elif (nomes[cont] == "FEIJOADA"):
		feijoada = feijoada +  1.27 * quantidade[cont]
	elif (nomes[cont] == "OMELETE"):
		omelete = omelete + 1.04 * quantidade[cont]
	elif (nomes[cont] == "TOMATE"):
		tomate = tomate + 0.2 * quantidade[cont]

	cont = cont + 1 
	
soma = banana +bife + feijoada + omelete + tomate

print (round (soma,2))
		
	


