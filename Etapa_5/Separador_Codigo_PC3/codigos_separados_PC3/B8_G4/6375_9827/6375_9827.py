from numpy import*

cand = input().upper().split(',')
vet= zeros(4, dtype = int)

for i in range(size(cand)):
	if cand[i] == 'A':
		vet[0] +=1
	elif	cand[i] == 'B':
		vet[1]+=1
	elif	cand[i] == 'C':
		vet[2] +=1
	elif	cand[i]== 'D':
		vet[3] +=1
print(vet)