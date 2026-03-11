from numpy import*
ps =input("Digite as iniciais dos paises:").upper().split(',')
vet= zeros(5, dtype=int)
for i in range(size(ps)):
	if(ps[i]=='CHN'):
		vet[0] = vet[0]+1
	elif(ps[i]=='JPN'):
		vet[1] = vet[1]+1
	elif(ps[i]=='KOR'):
		vet[2] = vet[2]+1
	elif(ps[i]=='MGL'):
		vet[3] = vet[3]+1
	elif(ps[i]=='THA'):
		vet[4] = vet[4]+1
print(max(vet))
print(vet)
		

