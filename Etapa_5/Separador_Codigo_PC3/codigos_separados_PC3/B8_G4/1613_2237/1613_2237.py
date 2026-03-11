from numpy import * 
A=array(eval(input("NOME : ")))
B=array(eval(input("gasto : ")))
i=0
soma=0
while (i< size(A)):
	if(A[i] == "ALONGAMENTO"):
		soma=soma+3*B[i]
	elif(A[i] == "CORRIDA"):
		soma=soma+10.3*B[i]
	elif(A[i] == "DANCA"):
		soma=soma+6.7*B[i]
	elif(A[i] == "ESCALADA"):
		soma=soma+9.7*B[i]
	elif(A[i] == "HIDROGINASTICA"):
		soma=soma+5.0*B[i]
	i=i+1
print(round(soma,2))