x = float(input("digite um numero real "))
k = int(input("qta de termos "))

a = 0 
i = 1

while(-1 < x < 1 and k > 0):
	soma =( -1)**a * (x * 2*i +1 + x* 2*i + 3 + 2*i + 5) / 2*i +1 + 2*i + 3 + 2*i + 5
	valor = soma * k
print(round(valor,7))