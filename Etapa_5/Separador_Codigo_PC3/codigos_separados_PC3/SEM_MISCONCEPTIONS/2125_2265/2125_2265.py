from numpy import *
n = array(eval(input("notas:")))

med = (n[0] * 3 + n[1] * 3 + n[2] * 4) / 10.0  

print(round(med, 2))

if(med >= 5):
	mensagem = "APROVADO"
else:
	mensagem = "REPROVADO"
print(mensagem)