from numpy import *
media = array(eval(input()))
NF = (media[0] * 2 + media[1] * 3 + media[2] * 5) / 10
print(round(NF, 2))
if(NF >= 5):
	mensagem = print("APROVADO")
else:
	mensagem = print("REPROVADO")



