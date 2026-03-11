from numpy import*
v= array(eval(input("Digite os vetores: ")))
s=0
for i in range(size(v)):
	if v[i] == 88:
		s= s/2
	else:
		s = s + v[i]
print(s)