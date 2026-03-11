num=int(input())
a=num//100
rest_a=num%100
b=a//100
rest_b=a%100
soma_dos_quadrados=(rest_a**2)+(rest_b**2)
if	(soma_dos_quadrados==num):
	mensagem=("atende")
	print(mensagem)
else:
	mensagem="nao atende"
	print(mensagem)
	
print(num)