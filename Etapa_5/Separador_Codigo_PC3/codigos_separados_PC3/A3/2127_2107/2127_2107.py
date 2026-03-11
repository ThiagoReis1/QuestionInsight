from numpy import*

notas=array(eval(input()))
								 
mfinal = (nota[0]+nota[1]+nota[2]+nota[3]-min(nota))/3.0

print(round(mfinal,2))

if(MFinal>50.0):
	print("APROVADO")
				
else:
	print("REPROVADO")
				
