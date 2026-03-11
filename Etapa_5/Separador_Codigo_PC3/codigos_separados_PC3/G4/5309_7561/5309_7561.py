x = float(input("numero real: "))
k = int (input("numero inteiro: "))
c = 0
while(c < k):
	x = x + (k-2)*x/(k+2)
	c = c + 1
print(round(k,8))
	