n = int (input("qual o termo da serie? "))
i = 1
s = 1
t = 0
while( i <= n):
	t = t + s * (i ** 2)/(1 + 2 * i + 1)
	s = -s 
	i = i + 1
print(round(t,7))	
	