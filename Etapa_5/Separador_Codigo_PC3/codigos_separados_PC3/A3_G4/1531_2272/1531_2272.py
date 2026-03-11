k = int(input("k:"))
n = int(input("n:"))
i = 1
serie = 1
s = -1

while(i<n):
	serie = serie + s * 2/((2*i)*(2*i-1)*(2*i+2))
	s = -s
	i = i + 1
x = 3 + serie
print(round(x,10))