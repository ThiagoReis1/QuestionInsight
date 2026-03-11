from numpy import*
vetor = array(eval(input("Informe o vetor: ")))
A = min(vetor)
B = max(vetor)
C = 0.85*A+0.15*B
D = 0.4*A+0.6*B
v = zeros(2, dtype = "int")
for i in vetor:
	if(i >= A and i < C):
		v[0] += 1
	elif(i >= D and i < B):
		v[1] += 1
print(v)