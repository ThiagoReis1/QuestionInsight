# Quantidade de praças de pedágio = q_p
# Valor do Pedágia em cada parada = 9,80
# Taxa de manutenção da estrada = 20,00

q_p = int(input("quantidade de pedagos: "))

valor = (9,8)
manutencao = (20,0)
imposto = (15/100)

valor_pedagio = ((q_p) * (valor))

valor_com_manutencao = (((valor_pedagio) + (manutencao))

valor_do_imposto = ((valor_com_manutencao) * (imposto))

total = ((valor_com_manutencao) + (valor_do_imposto))

print(round(total, 2))