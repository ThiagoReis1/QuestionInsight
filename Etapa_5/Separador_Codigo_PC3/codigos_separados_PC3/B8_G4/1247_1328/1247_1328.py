from numpy import*
vetor = array(eval(input("")))
A = min(vetor)
B = max(vetor)
C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B
v = zeros(2, dtype = int)
for i in vetor:
	if(i>= A and i < C):
		v[0]+=1
	elif(i>=D and i < B):
		v[1] +=1
print(v)