vol = float(input())

consumo_por_m3 = 0.37
taxa_fixa = 15
icms = 0.35

total = vol * consumo_por_m3 + 15

valor = total + total * icms

print(round(valor,2))