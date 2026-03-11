# Escrever o peso da mercadoria

peso = float(input("Digite o peso da mecadoria: "))

# Calcular o preço a ser pago (float)
# kg = custo por peso ; Tx = taxa fixa ; Icms = imposto

kg = 43.21
tx = 25
icms = 62/100

total_inicial = (kg * peso + tx)
icms_final = total_inicial * icms
total_final = total_inicial + icms_final
# Como saída o total a ser pago (print)

print(round(total_final,2))