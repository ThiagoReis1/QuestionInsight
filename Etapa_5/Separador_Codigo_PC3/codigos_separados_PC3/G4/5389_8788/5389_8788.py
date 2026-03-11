from numpy import*

s = input('digite a senha:').upper()

soma = 0

for i in range(len(s)):
	if s[i] == "A" or s[i] == 'E' or s[i]== 'I' or s[i] == 'O' or s[i]=='U':
		soma += 3.15
	else:
		soma += 4.17
		
	
	
print(round(soma,2))
		
	
	
