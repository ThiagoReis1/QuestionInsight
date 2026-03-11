n = int(input())
sd = 0
sinal = -1
a = 1
b = 1
i=1

while i <= n:
	sd=sd+sinal*(((a)**2)/(7+b))
	sinal=-sinal
	a=a+1
	b=b+2
	i=i+1
print(round(sd,11))