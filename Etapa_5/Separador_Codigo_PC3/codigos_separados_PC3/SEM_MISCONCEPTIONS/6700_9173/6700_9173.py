numero_de_dias = float(input(""))
aluguel_dia = 50.0
taxa_fixa = 30.0
total_sem_icms = aluguel_dia *numero_de_dias + taxa_fixa
porcentagem_icms = 18
aumento_icms = total_sem_icms *(porcentagem_icms/100)
total_com_icms = total_sem_icms + aumento_icms
print(round(total_com_icms,2))




