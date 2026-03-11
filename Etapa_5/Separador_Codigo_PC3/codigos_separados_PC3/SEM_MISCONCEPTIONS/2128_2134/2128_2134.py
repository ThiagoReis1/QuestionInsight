from numpy import*

a=array(eval(input("digite:")))

Mfinal=(sum(a)-max(a))/3.0
print(round(Mfinal,2))

if(Mfinal>=50):
	print("APROVADO")
else:
	print("REPROVADO")
	
