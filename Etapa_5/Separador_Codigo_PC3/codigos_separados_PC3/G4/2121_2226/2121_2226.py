from numpy import*

md=array(eval(input("notas: ")))
nt=((md[0]*5)+(md[1]*3)+(md[2]*2))/10
print(round(nt,2))
if(nt<=5):
	print("REPROVADO")
else:
	print("APROVADO")


