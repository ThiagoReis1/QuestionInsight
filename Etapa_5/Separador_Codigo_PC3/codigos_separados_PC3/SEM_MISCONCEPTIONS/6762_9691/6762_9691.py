# faça seu código aqui!
idade = int(input("insira a idadade: "))
i = 20.00
if idade < 12:
	t = 1.25 + i
elif idade == 12:
	t = 2.25 + i
elif idade > 12:
	t = 3.25 + i
else :
	t = "nao existe"
print(round(t,2))