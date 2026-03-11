from numpy import*
v = array((eval(input())))
notafinal = ((v[0]*5.0) + (v[1]*3.0) + (v[2]*2.0))/10
if(notafinal>=5):
	mensagem = "APROVADO"
else:
	mensagem = "REPROVADO"
print(round(notafinal,2))
print(mensagem)