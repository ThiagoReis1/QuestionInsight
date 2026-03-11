idade = int(input())
cont = 0
while (idade != -1):
	if (idade < 18):
		cont = cont + 1
	idade = int(input())	
print(cont)