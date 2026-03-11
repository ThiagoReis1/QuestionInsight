n= float(input("Digite um numero: "))
k= int(input("Digite o numero dos termos: "))

soma= 0
cont= 1

while(cont <= k):
	soma= soma - (((-1) ** cont)* ((n ** cont) / cont ))
	cont= cont + 1

print(round(soma, 10))
