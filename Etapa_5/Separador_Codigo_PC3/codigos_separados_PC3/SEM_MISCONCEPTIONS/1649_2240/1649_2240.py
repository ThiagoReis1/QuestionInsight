from numpy import*
cont = zeros(5, dtype=int)
vet = input("olhos: ").upper().split(',')
for i in arange(size(vet)):
	if vet [i] == 'P':
		cont[0] +=1
	elif vet [i] == 'C':
		cont[1] +=1
	elif vet [i] == 'M':
		cont[2] +=1
	elif vet [i] == 'V':
		cont[3] +=1
	elif vet [i] == 'A':
		cont[4] +=1	    
print(max(cont))
print(cont)
		
	
	
	
	
	
	
	
	from numpy import*
v = array(eval(input()))
i = 0
n = 0
for x in range(size(v)):
	if v[x]%2!=0:
		i = i + 1
		n = n + 1
	else:
		i = i + 1
k = size(v) - n
z = zeros(k,dtype=int)
i = 0
j = 0
for x in range(size(v)):
	if v[x]%2!=0:
		i = i + 1
	else:
		z[j]= v[x]
		j = j + 1
		i = i + 1
print(z)
