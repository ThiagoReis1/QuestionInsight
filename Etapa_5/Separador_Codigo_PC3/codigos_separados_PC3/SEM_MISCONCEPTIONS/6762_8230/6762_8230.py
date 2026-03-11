# faça seu código aqui!
idade = int(input("informe uma idade: "))

if (idade < 12):
	total = 20 + 1.25
elif (idade == 12):
	total = 20 + 2.25
else:
	total = 20 + 3.25
	
print(round(total, 2))