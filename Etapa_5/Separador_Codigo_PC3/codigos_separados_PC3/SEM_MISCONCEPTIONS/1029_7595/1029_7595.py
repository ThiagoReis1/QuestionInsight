valor_min = 0.28
valor_assin = 23

cons_chamada = float(input("Digite os minutos de chamada: "))
valor_cons1 = (valor_min * cons_chamada) + valor_assin
valor_imposto = valor_cons1 * (31/100)
valor_cons2 = valor_cons1 + valor_imposto

print(round(valor_cons2,2))