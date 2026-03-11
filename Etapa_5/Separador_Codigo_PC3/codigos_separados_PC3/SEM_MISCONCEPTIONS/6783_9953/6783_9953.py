anonasc=int(input())
pais=input().upper()
idade = 2023 - anonasc
if pais == "E":
	if idade >= 16:
		print("sim")
		print(idade - 16)
	else:
		print("nao")
		print(-idade+16)
elif pais == "B":
	if idade >= 18:
		print("sim")
		print(idade-18)
	else:
		print("nao")
		print(-idade+18)
else:
	print("invalido")