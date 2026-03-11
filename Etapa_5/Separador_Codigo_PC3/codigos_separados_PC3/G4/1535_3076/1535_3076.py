x = float(input("X: "))
k = int(input("K: "))

n = 0
i = 1
e = 0
arct = 0

while(n < k):
	arct = arct + (-1)**e * (x**i/i) 
	n = n + 1
	i = i + 2
	e = e + 1 

print(round(arct, 6))