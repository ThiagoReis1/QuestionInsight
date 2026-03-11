idade = int(input('digite uma idade: '))

total = 0 
x = 0

while (idade != -1):
	if idade < 18:
		x = x + 1
	total = total + 1
	idade = int(input('digite uma idade: '))

pm = (100 * x) / total

print(total)
print(round(pm,2))

	
