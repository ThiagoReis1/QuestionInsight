# faça seu código aqui!

x = input().upper()
i = 0
cont = 0

while i < len(x):
	if x[i] == 'B':
		cont+=1
	i+=1
	
print(cont)