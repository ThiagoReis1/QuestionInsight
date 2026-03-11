from numpy import*
s =  input('vetor po: ').split(',') #aqui coloca a string que vira vetor
v = zeros(6,dtype=int) #vetor contador
i = 0 #contador

for i in range(size(s)): #vai do primeiro elemento ate o ultimo
	if s[i] == 'MC': #verifica se o elemento do vetor string é igual a essa e...
		v[0] = v[0] + 1 #soma o elemento dessa posição do vetor contador mais 1 sempre que se repetir
	elif s[i] == 'C':
		v[1] = v[1] + 1
	elif s[i] == 'CM':
		v[2] = v[2] + 1
	elif s[i] == 'EM':
		v[3] = v[3] + 1
	elif s[i] == 'E':
		v[4] = v[4] + 1
	elif s[i] == 'ME':
		v[5] = v[5] + 1
	i = i + 1
print(max(v))
print(v)