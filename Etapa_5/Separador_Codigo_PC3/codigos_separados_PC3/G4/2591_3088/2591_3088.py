from numpy import*
v = array(eval(input("Insira as ocorrencias de acidentes: ")))
n = -v[0]
t = 0
for i in range(size(v)):		
	if v[i]<=n and v[i]!=v[0]:
		print(i)
		t = t + 1
print(t)

	 
	