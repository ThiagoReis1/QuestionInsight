# Peso do saco de ração = p_sr
# Quantidade diária de ração = q_dr

p_sr = float(input("p_sr: "))
q_dr = float(input("q_dr: "))

Semana = (q_dr) * 7
Resto = (p_sr - Semana)

print(round(Resto, 2))