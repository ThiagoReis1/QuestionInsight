x = float(input("real: "))
k = int(input("quantidade de termos: "))

soma = 0
i = 1

while i <= k :
	soma = soma + i
	i = i + 1
	
s = soma*(1/x)

print(round(s,10))