telefone = float(input("Digite o consumo de chamada: "))
Valorpormin = telefone * 0.28
valorassinatura = Valorpormin + 23.00
Valoricms = valorassinatura*(31/100)
total = valorassinatura+Valoricms
print(round(total , 2))