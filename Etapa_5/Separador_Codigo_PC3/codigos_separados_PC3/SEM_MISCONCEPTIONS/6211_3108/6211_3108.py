integer = int(input())
ocorrencias = 0
while(integer != -1):
	if((100 <= integer) and (integer <= 199)):
		ocorrencias = ocorrencias + 1
	integer = int(input())
print(ocorrencias)