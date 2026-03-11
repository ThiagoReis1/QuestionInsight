from numpy import*

est = input().upper().split(',')
vet = zeros(5 ,dtype=int)

for i in est:
	if(i == "AC"):
	   vet[0]+= 1
	if(i == "AM"):
		vet[1]+= 1
	if(i == "PA"):
		vet[2]+=1
	if(i == "RO"):
		vet[3]+=1
	if(i == "RR"):
		vet[4]+=1
	
print(max(vet))
print(vet)


	

	