from numpy import*
a= array(eval(input("Digite o vetor de nomes de alimentos: ")))
q= array(eval(input("Digite o vetor da quantidade em gramas: ")))
i= 0
j= 0
while(i<size(q)):
	if(a[i]=="BANANA"):
		j= j + 0.97 * q[i]
	elif(a[i]=="BIFE"):
		j= j + 2.95 * q[i]
	elif(a[i]=="FEIJOADA"):
		j= j + 1.27 * 
	elif(a[i]=="OMELETE"):
		j= j + 1.04
	elif(a[i]=="TOMATE"):
		j= j + 0.2
	i= i + 1
prato= 