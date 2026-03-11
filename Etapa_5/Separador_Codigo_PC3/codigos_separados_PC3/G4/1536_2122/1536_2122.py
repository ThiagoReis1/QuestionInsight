i = 1
s = 0
sinal = 1
x= float(input())
k = int(input())
j = 0
while(j<k):
	termo = (x**i/i)*sinal
	s = s + termo
	sinal = -sinal
	i = i + 1
	j = j + 1
print(round(s-x+1,10))