numero = int(input())
p= input().upper()
idade =2023 - numero
if p =="B":
	im = 21
	if idade >=im:
		print("sim")
		print(idade - im)
	else:
		print("nao")
		print(im - idade)
elif p == "R":
	im=18
	if idade>=im:
		print("sim")
		print(idade - im)
	else:
		print("nao")
		print(im - idade)
else:
	print("invalido")
			