minutos_excedentes = float(input())
valor_sem_icms = 45.0 + 0.97 * minutos_excedentes
valor_com_icms = valor_sem_icms * 1.42
print(round(valor_com_icms, 2)) 
