# faça seu código aqui!
net = float(input(": "))
if net < 50:
	gaato = 60.0 + 4.50
elif net == 50:
	gaato = 60.0 + 5.50
else:
	gaato = 60.0 + 6.50
print(round(gaato,2))