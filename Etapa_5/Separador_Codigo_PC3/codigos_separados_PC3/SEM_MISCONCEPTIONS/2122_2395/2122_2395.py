from numpy import*
n = array(eval(input("notas parciais: ")))

nf = ((n[0]*2)+(n[1]*3)+(n[2]*5))/10
print(round(nf, 2))
if(nf>=5):
	mensagem = "APROVADO"
else:
	mensagem = "REPROVADO"
print(mensagem)
