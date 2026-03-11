from numpy import*
v = array(eval(input("")))
cont = 0
for i  in range(size(v)):
	if(v[i] % 2 != 0):
		cont = cont + 1
newv = zeros(cont,dtype=int)
i = 0
for j in range(size(v)):
	if(v[j]%2!=0):
		newv[i] = j
		i = i + 1
print(cont)
print(newv)
		
	