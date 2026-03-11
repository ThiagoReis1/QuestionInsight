consumo = float( input() )

custo_min = 0.28
fixo = 23.00
ICMS = (31/100)

valor_final = (consumo*custo_min) + fixo 
valor_final += valor_final * ICMS

print(round( valor_final, 2 ))