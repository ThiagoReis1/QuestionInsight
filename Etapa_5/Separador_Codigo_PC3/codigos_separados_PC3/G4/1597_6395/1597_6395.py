from numpy import*

V = array(eval(input("Digite: ")))

i = 0

for i in range(size(V)):
	if V[i] > 80:
		V[i] = V[i]  - 5

print(round(sum(V),2)) 




