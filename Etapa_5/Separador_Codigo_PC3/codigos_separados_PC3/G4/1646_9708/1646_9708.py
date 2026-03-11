from numpy import*
s = array(eval(input()))
cont = 0
for i in range(size(s)):
	if s[i] <= 50:
		cont +=1
print(cont)
aux = zeros(cont,dtype=int)
j = 0
for i in range(size(s)):
	if s[i] <= 50:
		aux[j] = i
		j +=1
print(aux)
	