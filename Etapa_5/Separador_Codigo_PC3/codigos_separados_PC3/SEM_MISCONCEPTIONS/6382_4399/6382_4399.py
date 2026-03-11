from numpy import *
mensagem = array(eval(input()))
for i in range(size(mensagem)):
	if mensagem[i] == 9:
		mensagem[i] = 0
	else:
		mensagem[i] = (mensagem[i]+1)**2
print(mensagem)