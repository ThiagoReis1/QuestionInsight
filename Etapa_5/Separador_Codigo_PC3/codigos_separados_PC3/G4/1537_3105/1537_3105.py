from math import*
numero=float(input())
k=int(input())
soma=0
deno=0
expo=0
while (expo<k):
	soma=soma+numero**expo/factorial(deno)
	expo=expo+1
	deno=deno+1
print(round(soma, 9))
