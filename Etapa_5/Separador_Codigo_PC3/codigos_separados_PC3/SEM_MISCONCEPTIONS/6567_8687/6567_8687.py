# faça seu código aqui!
v_i = int(input("Velocidade de internet: "))

if v_i == 50:
	valor = 5.5 + 60
elif v_i < 50:
	valor = 4.5 + 60
else:
	valor = 6.5 + 60
print("total=", valor)