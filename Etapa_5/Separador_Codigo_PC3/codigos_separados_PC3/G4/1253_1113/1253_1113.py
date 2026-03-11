from numpy import *
vetor = array(eval(input("Digite o vetor: ")))
A = min(vetor)
B = max(vetor)

x = zeros(2, dtype = "int")

C = 0.6 * A + 0.4 * B
D = 0.3 * A + 0.7 * B


for i in range(0,size(vetor)):
	if( vetor[i] >= A and vetor[i] < C):
		x[0] = x[0] + 1

for i in range(0, size(vetor)):
	if(vetor[i] >= D and vetor[i]< B):
		x[1] = x[1] + 1
 
print(x)
		
	
	