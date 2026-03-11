ano = int(input())
pais = input().upper()
idade = 2023 - ano
if pais == "B" and idade >= 18:
	print("sim")
	print(idade-18)
elif pais == "B" and idade < 18:
	print("nao")
	print(18-idade)
elif pais == "R" and idade >= 21:
	print("sim")
	print(idade-21)
elif pais == "R" and idade < 21:
	print("nao")
	print(21-idade)	
else:
	print("invalido")