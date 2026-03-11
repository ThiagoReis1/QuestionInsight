from numpy import*
nota=array(eval(input("notas do aluno: ")))
i =0
	
media= (nota[0]*3+nota[1]*3+nota[2]*4)/10
if(media>=5.0):
	print(round(media, 2))
	print("APROVADO")	

else:
	print(round(media,2))
	print("REPROVADO")