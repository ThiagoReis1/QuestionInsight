agua = float(input("Quantidade de agua consumida no mes: "))
custo = 0.37
taxa = 15
icms = 35/100

consumo = agua * custo + taxa
conta = consumo * icms
conta_final = conta + consumo



print(round(conta_final,2))