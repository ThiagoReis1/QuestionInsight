# faça seu código aqui!
net = int(input("Velocidade da internet: "))

if net < 50:
	cont = 60+ 4.5
elif net == 50:
	cont = 60 + 5.5
else:
	cont = 60 + 6.5
print("total=", cont)	