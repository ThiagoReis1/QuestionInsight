ano = int(input("qual seu ano: "))
pais = input("qual seu pais de nascimento (B/R): ").upper()

if pais != "B" and pais != "R":
	print("invalido")

ida = 2023 - ano
if pais == "R" and ida >= 18:
	print("sim")
	if ida >= 18:
		print(ida - 18)
	else:
		print("nao")
		print(18 - ida)
idade = 2023 - ano

if pais == "B" and idade >= 21:
	print("sim")
elif idade >= 21:
	print(idade - 21)
else:
	print("nao")
	print(21 - ida)







	






 