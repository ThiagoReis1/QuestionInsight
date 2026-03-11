from numpy import*
a = input(" ").upper().split(",")
v = zeros(5,dtype=int)
for sigla in a :
	if sigla == "B":
		v[0]= v[0]+1
	elif sigla == "PA":
		v[1]= v[1]+1
	elif sigla == "PR":
		v[2]= v[2]+1
	elif sigla == "A":
		v[3]=v[3]+1
	elif sigla == "I":
		v[4]=v[4]+1
print(max(v))
print(v)