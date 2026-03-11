from numpy import*
nota = array(eval(input(" ")))

i = 0
soma = 0
while(i<4):
	soma = soma + nota[i]
	i = i + 1
media = (soma - max(nota))/3
print(round(media,2))
if(media<50):
	print("REPROVADO")
elif(media>=50):
	print("APROVADO")