contadora = 0
numero = int(input())

while numero != -1:
	if 26<= numero <= 85:
		contadora += 1
	numero = int(input())
	
print(contadora)