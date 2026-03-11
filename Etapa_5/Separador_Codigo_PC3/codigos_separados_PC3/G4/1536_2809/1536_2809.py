#serie de maclaurin 

x = float(input(':'))
k = int(input(':'))

i = 0
soma = 0

while (i < k):
	soma = soma + (-1)**(i)* (x**(i+1))/(i+1)
	i = i + 1
print(round(soma, 10))