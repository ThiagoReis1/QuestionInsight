t_s = input().upper()
qnt = int(input("Qntdd de tapiocas ou salgados: "))
acai = int(input("Qntdd de acai: "))

tapioca = qnt * 5.5
salgado = qnt * 4
acai1 = acai * 10

if t_s == "T":
	total = float(tapioca + acai1)
	print(round(total, 1))

elif t_s == "S":
	total = float(salgado + acai1)
	print(round(total, 1))
	
else:
	print("Voce digitou errado!")