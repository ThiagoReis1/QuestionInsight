from numpy import*
tomp = input("informe tom da pele").split(',')
vet = zeros(6,dtype=int)

for i in range(len(tomp)):
	if tomp[i] =='MC':
		vet[0]=vet[0]+1
	if tomp[i] =='C':
		vet[1]=vet[1]+1
	if tomp[i] =='CM':
		vet[2]=vet[2]+1
	if tomp[i] =='EM':
		vet[3]=vet[3]+1
	if tomp[i] =='E':
		vet[4]=vet[4]+1
	if tomp[i] =='ME':
		vet[5]=vet[5]+1
print(max(vet))
print(vet)	
