peso = float(input())

if (peso >= 5000):
	frete=0.04*peso + 60
else:
	frete=0.05*peso

print(round(frete, 2))