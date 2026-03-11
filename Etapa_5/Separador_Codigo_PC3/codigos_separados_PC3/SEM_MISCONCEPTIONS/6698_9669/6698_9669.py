quant = int(input("Entre com a quantidade de pracas de pedagios no caminho = "))

valor_sem_imposto = (9.80 * quant) + 20

valor_com_imposto = valor_sem_imposto + 15/100 * valor_sem_imposto

print(round(valor_com_imposto, 2))