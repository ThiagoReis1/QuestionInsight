from numpy import*

v = array(eval(input("Digite o Vetor: ")))
p = 0
s = 0
B = max(v)
A = min(v)

C = 0.75*A + 0.25*B
D = 0.25*A + 0.75*B

for i in range(0, size(v)):
	if(A <= v[i] and C > v[i]):
		p = p + 1
	elif(D <= v[i] and B > v[i]):
		s = s + 1
x = array([p, s])
print(x)