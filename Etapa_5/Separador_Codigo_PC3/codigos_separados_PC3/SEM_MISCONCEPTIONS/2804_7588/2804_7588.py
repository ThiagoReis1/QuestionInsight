aporte0 = int(input())
meses = int(input())

i = 1

rendimento = aporte0 + (aporte0 * 0.01)
print(rendimento)

while(i < meses):
	rendimento += (rendimento * 0.01)
	i += 1
	print(round(rendimento, 2))