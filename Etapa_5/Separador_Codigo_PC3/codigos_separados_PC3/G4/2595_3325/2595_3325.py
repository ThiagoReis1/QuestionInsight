from numpy import*
v = array(eval(input("vetor demanda: ")))
q = 0
for i in range(1,size(v)):
	if(v[i]<=v[0]):
		q = q +1
		print(q)
print()