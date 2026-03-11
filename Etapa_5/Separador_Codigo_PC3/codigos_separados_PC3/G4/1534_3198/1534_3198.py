x = float(input())
k = float(input("Coloque as repeticoes"))
s = 0
soma = 0
e = 1
			 
while (s < k):
	termo =  (x ** (e)/(e)) 
	soma = soma + termo
	e = e + 2
	s = s + 1
print(round(soma,7))