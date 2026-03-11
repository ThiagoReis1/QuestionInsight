c = 200000
d = 50000
m = 1000
j = 0.65
j = j/100
soma = d
t = 0 
if(c>0 and d>0 and m>0 and j>0):
	while(soma < c):
		soma = round(soma, 2)
		soma = soma + m
		soma = soma * j
		t = t + 1
else:
	t = "Dados incorretos"
print(t)