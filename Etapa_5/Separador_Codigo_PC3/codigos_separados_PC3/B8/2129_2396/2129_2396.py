from numpy import*
vet=array(eval(input()))
mfinal=(vet[0]*1.0+vet[1]*2.0+vet[2]*3.0+vet[3]*4)/10.0
if(mfinal>5):
	print(round(mfinal, 2))
	print("APROVADO")
elif(mfinal<5):
	print(round(mfinal, 2))
	print("REPROVADO")
