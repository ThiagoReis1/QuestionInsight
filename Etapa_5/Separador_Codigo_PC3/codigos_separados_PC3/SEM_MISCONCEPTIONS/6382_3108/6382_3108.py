from numpy import *

mensagem = array(eval(input()))

#codificação
for i in range(len(mensagem)):
	mensagem[i] = ((mensagem[i] + 1) % 10) ** 2
	
print(mensagem)