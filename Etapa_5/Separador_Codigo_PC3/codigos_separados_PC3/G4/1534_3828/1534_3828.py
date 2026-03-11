x = float(input("digite real x: "))
k = int(input("digite quantidade de termos: "))

soma = 0 # valor acumuladora
i = 0 # valor contadora

#if (x >= -1) and (x <= 1) and (k > 0):
while (i < k):
	soma = soma + (x**(2*i + 1))/(2*i + 1)
	i = i + 1
print (round(soma, 7))
		