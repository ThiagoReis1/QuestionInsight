consumo_de_chamadas_por_minutos= float(input(""))
plano= (0.28 * consumo_de_chamadas_por_minutos) + 23
total= (31/100 * plano) + plano
print(round(total,2))
