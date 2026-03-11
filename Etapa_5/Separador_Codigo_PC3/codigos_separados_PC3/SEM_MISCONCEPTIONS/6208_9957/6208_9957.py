numero = int(input())
sorte  = 0

while numero != -1:
	numero = int(input())
	
	if numero < 76 and numero > 50:
		sorte += 1
		
print(sorte)