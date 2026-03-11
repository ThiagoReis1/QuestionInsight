from numpy import*
v = array(eval(input("digite o vetor: ")))
A = min(v)
B = max(v)
C = (0.85*A + 0.15*B)
D = (0.4*A + 0.6*B)
		  
cont = array(zeros(2, dtype = int))
for i in range(size(v)):
	if(v[i] >= A and v[i] < C):
		  cont[0] = cont[0] + 1
	elif(v[i] >= D and v[i] < B):
		  cont[1] = cont[1] + 1
			
print(cont)
		
	
