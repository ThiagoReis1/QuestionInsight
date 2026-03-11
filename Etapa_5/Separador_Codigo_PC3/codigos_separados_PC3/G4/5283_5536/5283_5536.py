n = int(input())

pos = int(0)
soma = int(0)

while (n != 0):
	
	if(n > 0):
		pos = pos + 1
		
	soma = soma + 1
	n = int(input())
	
print(soma)
print(round(pos/soma*100, 2))