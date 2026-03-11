from numpy import *
vet = array(eval(input("qual o vetor: ")))
v = array([0,0])
A = max([vet])
B = min([vet])
C = 0.65 * A + 0.35 * B
D = 0.45 * A + 0.55 * B
while(x < 1):
for x in range(size(vet)):
	if( x >= A and x <= C):
		v[0] = v[0] + 1
	elif(x >= C and x < D):
		v[1] = v[1] + 1
print(v)