# faça seu código aqui!
peso = float(input("insira o peso do pacote: "))

fixo = 10   #variavel para taxa fixa para o envio de pacotes
total = 0   #variavel acumuladora
if peso < 5:
	total = fixo + 3.75
elif peso == 5:
	total = fixo + 4.75
else:
	total = fixo + 5.75

print(round(total, 2))