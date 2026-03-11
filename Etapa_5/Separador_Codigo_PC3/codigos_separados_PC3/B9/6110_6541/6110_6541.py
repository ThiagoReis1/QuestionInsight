combustivel = float(input())

if combustivel < 17.5:
	combustivel = combustivel + 10.5
elif combustivel >= 17.5 and combustivel < 35.0:
	combustivel = combustivel + 14.0
elif combustivel >= 35.0 and combustivel < 50.0:
	combustivel = combustivel + 18.6
else:
	combustivel = combustivel + 24.5

print(round(combustivel, 3))