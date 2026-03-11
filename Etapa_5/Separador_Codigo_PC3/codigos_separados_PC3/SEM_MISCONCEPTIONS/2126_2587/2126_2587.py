from numpy import *
n = array(eval(input("notas:")))

med = (n[0] * 5 + n[1] * 2.5 + n[2] * 2.5) / 10.0  

print(round(med, 2))

if(med >= 5):
	mensagem = "APROVADO"
else:
	mensagem = "REPROVADO"
print(mensagem)
