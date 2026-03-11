x = float(input())
k = int(input())
soma = 0
cont = 1
ed = 3
while(cont < k):
	soma = soma + (x ** ed)/ed
	cont = cont + 1
	ed = ed + 2
print(round(x + soma, 7))
	