from numpy import *
GELO = "GELO"
FOGO = "FOGO"
CHOQUE = "CHOQUE"
CONJURACAO = "CONJURACAO"
ILUSAO = "ILUSAO"
tipo = array(eval(input("Tipo de magia: ")))
nivel = array(eval(input("Nivel do mago: ")))
i = 0
soma = 0
if(size(tipo) == size(nivel)):
	while(i<size(nivel)):
		if(tipo[i] == "GELO"):
			soma = soma + 2*nivel[i]
			i = i + 1
		elif(tipo[i] == "FOGO"):
			soma = soma + 3*nivel[i]
			i = i + 1
		elif(tipo[i] == "CHOQUE"):
			soma = soma + 4*nivel[i]
			i = i + 1
		elif(tipo[i] == "CONJURACAO"):
			soma = soma + 8*nivel[i]
			i = i + 1
		elif(tipo[i] == "ILUSAO"):
			soma = soma + 10*nivel[i]	
			i = i + 1
print(soma)
