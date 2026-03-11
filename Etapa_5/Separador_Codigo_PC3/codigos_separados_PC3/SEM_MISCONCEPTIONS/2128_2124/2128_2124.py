from numpy import*
nota=array(eval(input("Digite um numero:")))
Mfinal=(sum(nota)-max(nota))/3.0
print(round(Mfinal,2))
		  
if(Mfinal>=50.0):
	print("APROVADO")
else:
	print("REPROVADO")


