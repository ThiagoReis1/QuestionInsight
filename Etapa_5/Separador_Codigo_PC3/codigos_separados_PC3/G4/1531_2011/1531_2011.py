from math import * 
x = eval(input("angulo em radianos:  "))
k = int(input("quantidade de termos da série:  "))

i=0
cos=1
s = +1
while(i < k):
	cos = cos + (s)*x**(2*i)/factorial(2*i)
	s = -s
	i = i + 1
	
print(round(cos-1, 10))