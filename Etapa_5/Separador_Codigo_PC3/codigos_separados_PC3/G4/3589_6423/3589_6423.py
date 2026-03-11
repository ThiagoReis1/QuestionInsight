from numpy import*
x = array(eval(input("Vetor de números")), dtype=int)
i = 0
s = 0
for x[i] in x:
	if x[i]==1:
		s += 80
	if x[i]==2:
		s+= 40
	if x[i]==3:
		s+=20
	if x[i]==4:
		s+=10
	i +=1
print(s)
	