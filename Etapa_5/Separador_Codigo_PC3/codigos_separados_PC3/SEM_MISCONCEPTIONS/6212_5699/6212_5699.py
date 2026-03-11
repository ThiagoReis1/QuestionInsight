num = int(input())
saudaveis = 0

while num != -1:
	if num>=26 and num<=85:
		saudaveis+=1
	num = int(input())

print(saudaveis)