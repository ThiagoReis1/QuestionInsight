from numpy import*
s=input("pais: ").upper().split(',')

vet= zeros (5,dtype=int)

for i in range(size(s)):
	if(s[i]=="BE"):
		vet[0]=vet[0]+1
	elif(s[i]=="ES"):
		vet[1]=vet[1]+1
	elif(s[i]=="FR"):
		vet[2]=vet[2]+1
	elif(s[i]=="IT"):
		vet[3]=vet[3]+1
	elif(s[i]=="PT"):
		vet[4]=vet[4]+1

for i in range(size(s)):	
	if(s[i]=="BE"):
		vet[0]=vet[0]+1
	elif(s[i]=="ES"):
		vet[1]=vet[1]+1
	elif(s[i]=="FR"):
		vet[2]=vet[2]+1
	elif(s[i]=="IT"):
		vet[3]=vet[3]+1
	elif(s[i]=="PT"):
		vet[4]=vet[4]+1
		print(i)
print(vet)
		     


		
		