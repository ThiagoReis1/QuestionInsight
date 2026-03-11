n = float(input("Quantos termos? "))
d = 1
s = 0 
i = 3
sinal = 1
while(a<n):
	s=s+(b**3/(2+i))*sinal
	i=i+2
	b=b+1
	sinal=sinal*-1
	n=n+1
print(round(s,8))