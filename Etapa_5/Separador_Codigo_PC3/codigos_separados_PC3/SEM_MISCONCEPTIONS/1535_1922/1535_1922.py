x = float(input())
k = float(input())
sinal = +1
i = 0
arctg = 0
while(i < k):
	arctg = arctg + sinal*(x**(2*i + 1))/(2*i+1)
	sinal = -sinal
	i = i + 1
print(round(arctg,6))
	
