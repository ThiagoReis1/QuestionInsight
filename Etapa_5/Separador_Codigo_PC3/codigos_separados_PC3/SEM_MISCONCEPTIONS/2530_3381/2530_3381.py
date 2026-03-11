D=float(input())
TF=float(input())
j=float(input())

final=D+D*0.15
valor=D
mes=0

if(D>0 and TF>0 and j>0):
	while(valor<=final):
		valor=valor+D*(j/100)-TF
		mes=mes+1
	print(round(mes,2))
else:
	print("Dados incorretos")