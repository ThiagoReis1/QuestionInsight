from numpy import*

vet= array(eval(input("digite o vetor:")))
vetx= array(zeros(2,dtype=int ))
A = min(vet)
B = max(vet)
C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 *B 
for i in vet:
	if(vet(i)>=A and vet(i)<C):
		vetx[0]=vetx[0] +1

	elif(vet(i)>=D and vet(i)<B):
		vetx[1]=vetx[1] + 1
	else:
		
	print(vetx[0])
	print(vetx[1])

  
	
	
	
	
	