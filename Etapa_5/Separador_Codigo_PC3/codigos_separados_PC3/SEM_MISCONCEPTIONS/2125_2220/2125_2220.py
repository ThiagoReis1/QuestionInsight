from numpy  import*
notas=array(eval(input("notas das 3 atividades: ")))

notaf=((notas[0]*3.0)+(notas[1]*3.0)+(notas[2]*4.0))/10.0
if(notaf >= 5.0):
	mensagem="APROVADO"
else:
	mensagem="REPROVADO"
print(round(notaf,2))
print(mensagem)