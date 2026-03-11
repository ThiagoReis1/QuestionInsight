from numpy import *
st = input("digite uma string: ")
nivel = array(eval(input("digite um vetor: ")))
i = 0
espada = len(st)
while (i < espada):
	if(espada[i] == "CENOURA"):
		mensagem = 2*nivel[i]
	i += 1
print(mensagem)
		
