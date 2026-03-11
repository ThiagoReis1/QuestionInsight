from numpy import*

nota = array(eval(input("digite as notas: ")))

mf = (nota[0]*5.0 + nota[1]*2.5 + nota[2]*2.5)/10.0

if(mf > 5.0):
	mensagem = "APROVADO"
else:
	mensagem = "REPROVADO"

print(round(mf,2))
print(mensagem)


