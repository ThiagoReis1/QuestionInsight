from numpy import*
from numpy.linalg import*
S = input("strig: ").upper().split(',')
C = zeros(5,dtype=int)
for i in range(len(S)):
	if S[i]=='P':
		C[0] = C[0] + 1
	elif S[i] == 'C':
		C[1] = C[1] + 1
	elif S[i] == 'M':
		C[2] = C[2] + 1
	elif S[i]=='V':
		C[3] = C[3] + 1
	elif S[i]=='A':
		C[4] = C[4] + 1 
print(max(C))
print(C)
		
	
		
	
		
	