numero=int(input())
pais=input().upper()
idade=2023-numero
if pais=="B":
	idade_minima=18
	if idade >= idade_minima:
		print("sim")
		print(idade-18)
	else:
		print("nao")
		print(18-idade)
elif pais=="R":
	idade_minima=17
	if idade>=idade_minima:
		print("sim")
		print(idade-17)
	else:
		print("nao")
		print(17-idade)
else:
	print("invalido")