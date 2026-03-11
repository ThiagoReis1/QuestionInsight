from numpy import*
nome = array(eval(input("")))
vet = array(eval(input("")))
i=0
cal=0
while(i<size(vet)):
	if(nome[i]=='BANANA'):
		cal = cal+ 0.97*vet[i]
	elif(nome[i]=='BIFE'):
		cal = cal +2.97*vet[i]
	elif(nome[i]=='FEIJOADA'):
		cal = cal+1.27*vet[i]
	elif(nome[i]=='OMELETE'):
		cal = cal+1.04*vet[i]
	elif(nome[i]=='TOMATE'):
		cal = cal+0.2*vet[i]
	i=i+1
print(round(cal,2))
	