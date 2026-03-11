n = float(input("Numero da sorte: "))
c = 0

while n >= 0:
	if(n>=51 and n<= 75):
		c = c + 1
		n = float(input("Numero da sorte: "))
	else:
		n = float(input("Numero da sorte: "))
print(c)