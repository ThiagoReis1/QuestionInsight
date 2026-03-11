tempo_investimento = int(input("tempo de investimento ")) 

Qf = 1042000
Qi = 1500
i = ((Qf/Qi)**(1/tempo_investimento))-1

print(round(i,5))