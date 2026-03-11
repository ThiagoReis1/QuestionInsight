tempo = float(input("Digite o tempo de estacionamento em horas: "))

taxa_estacionamento = 15
limpeza = 5
icms = 20/100

total = (tempo * taxa_estacionamento) + limpeza 
total1 = total + total*icms

total = print(round(total1 , 2))
