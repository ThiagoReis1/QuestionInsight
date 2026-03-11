from numpy import*

st=input().split(',')
vetor=zeros(5,dtype=int)
for i in range(len(st)):
	if(st[i]=="AM"): 
		vetor[0]=vetor[0]+1
	elif (st[i]=="PE"):
		vetor[1]=vetor[1]+1
	elif (st[i]=="MG"):
		vetor[2]=vetor[2]+1
	elif (st[i]=="SP"):
		vetor[3]=vetor[3]+1
	else:
		vetor[4]=vetor[4]+1
		
print(max(vetor))
print(vetor)