numero = int(input())
noIntervalo = 0

while(numero != -1):
	if(numero >= 26 and numero <=50):
		noIntervalo += 1
	numero = int(input())

print(noIntervalo)