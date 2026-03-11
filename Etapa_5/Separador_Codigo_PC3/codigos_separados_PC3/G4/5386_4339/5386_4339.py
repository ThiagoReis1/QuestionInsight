from numpy import *
v= array()
print(v)
i=0
cont=0
while i < size[v]:
	if (v[i] == "A") or (v[i] == "E") or (v[i] == "I") or (v[i] == "o") or (v[i] == "u") :
		cont=cont + 1.12
	if (v[i] != "a") or (v[i] != "E") or (v[i] != "I") or (v[i] != "o") or (v[i] != "u") :
		cont= cont + 1.18
	i=i+1
print(round(cont,2))

