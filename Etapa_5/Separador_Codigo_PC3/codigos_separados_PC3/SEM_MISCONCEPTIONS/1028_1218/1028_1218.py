# UNIVERSIDADE FEDERAL DO AMAZONAS
# NOME: NANCY FREITAS DA SILVA
# DATA: 15/06/16
# PROGRAMA: CUSTO DO CONSUMO DE ÁGUA

volume_agua = float(input("Indique o volume de água consumido: "))
consumo1 = (volume_agua * 0.37) + 15.00 # valor de consumo a ser pago sem a taxa de icms
consumo_com_icms = consumo1 + (consumo1 * 0.35) # valor total a ser pago
print(round(consumo_com_icms,2))