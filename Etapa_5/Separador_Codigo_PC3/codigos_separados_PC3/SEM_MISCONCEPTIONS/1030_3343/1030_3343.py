minutos = float(input("mim:"))

plano = 45

minutos_excedentes = 0.97 * minutos

total = plano + minutos_excedentes + (plano + minutos_excedentes) * 42/ 100

print(round(total , 2))