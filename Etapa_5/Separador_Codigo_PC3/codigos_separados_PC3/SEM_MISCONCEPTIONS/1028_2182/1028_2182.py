N =float(input("litros ?"))
custo = 0.37
tx_de_tra = 15.00
icms = 35/100
conta1 = (N * custo + tx_de_tra)*icms
conta = (N * custo + tx_de_tra)
valor = conta + conta1
print(float(round(valor, 2)))


