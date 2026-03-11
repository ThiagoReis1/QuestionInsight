from numpy import*
v = array(eval(input("asd")), dtype=int)
i = 0
j = 0
k = 0
s = 0
while k!=size(v):
	if v[k]%3==0:
		i+=1
	k+=1
	
v2 = zeros(i, dtype=int)
while j!=size(v):
	if v[j]%3==0:
		v2[s] = j
		s+=1
	j+=1

print(i)
print(v2)

