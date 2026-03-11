v_cons = float(input("valor consumido:"))
kwh_cons = (0.43 * v_cons) + 10
porcentagem = (kwh_cons) * 25/100
total = kwh_cons + porcentagem
print(round(total, 2))