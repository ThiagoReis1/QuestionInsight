x = float (input())
k = int (input())

exp = ((k * 2) - 1)
if (k % 2 == 0):
	sinal = -1
else:
	sinal = 1
arctg = 0
	
while (exp >= 1):
	termo = (sinal * ((x ** exp) / exp))
	arctg = arctg + termo
	sinal = sinal * -1
	exp = exp - 2
	
print (round (arctg, 6))
	
	