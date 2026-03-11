from math import*
x = float(input("insira um nr:"))
k = int(input("insira um ni:"))
i = 1
signal = 1
soma = 0
while(i<=k):
	soma = soma + signal*(x**i)/(i)
	i = i+1
	signal = -1*signal
print(round(soma-x+1,10))