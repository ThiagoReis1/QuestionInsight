from numpy import*

#Vetor de strings:
string = input("Países: ").split(',')

#Vetor de contagem:
zero = zeros(5, dtype=int)

#Contagem:
for i in range(size(string)):
	if(string[i] == 'CHN'):
		zero[0] += 1
		
	elif(string[i] == 'JPN'):
		zero[1] += 1
		
	elif(string[i] == 'KOR'):
		zero[2] += 1
		
	elif(string[i] == 'MGL'):
		zero[3] += 1
		
	elif(string[i] == 'THA'):
		zero[4] += 1
		
print(max(zero))		
print(zero)