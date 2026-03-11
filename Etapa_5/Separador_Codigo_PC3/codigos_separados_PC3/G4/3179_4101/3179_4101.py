from numpy import*
v1 = array(eval(input("Valores do Vetor: ")))
v2 = zeros(size(v1), dtype=int)
t = 0
for i in range(size(v1)):
	if(v1[i]!=1):
		v2[t] = v1[i]
		t +=1
g = size(v1) - 1
for i in range(size(v1)):
	if(v1[i]==1):
		v2[g]=v1[i]
		g -= 1
print(v2)
		
		