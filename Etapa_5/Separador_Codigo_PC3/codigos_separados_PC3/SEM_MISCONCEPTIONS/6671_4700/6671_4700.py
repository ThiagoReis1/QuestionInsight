from numpy import *
entrada = array(eval(input ("Digite a sequencia: ")))

soma = 0
contagem = 0

for i in entrada:
	if i > 15:
		soma += i
		contagem += 1

if contagem > 0:
	media = soma/contagem
else:
	media = 0
print(round(media,2))
	
		
