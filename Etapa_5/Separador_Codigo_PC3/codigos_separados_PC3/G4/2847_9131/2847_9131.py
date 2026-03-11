from numpy import*
v = array(eval(input("digite o vetor:")))
for i in range(size(v)):
   if v[i] == 0:
      v[i] = v**2

print(v**2)
	