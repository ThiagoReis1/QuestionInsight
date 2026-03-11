aluguel = 50
taxa= 30
dias= float(input("numero de dias: "))

valor = aluguel * dias + taxa 
icms= valor * (18/100) + valor 

print(round(icms, 2))
