#Wagner William Amorim - Matricula 21552149
#Primeira Avaliação
#Exercicio 2
#16/06/2016

valor_da_conta = float(input("Qual o valor da conta esse mes ? "))

valor_da_conta_real = round (valor_da_conta * 0.43, 2)

consumo = (valor_da_conta_real + 10.00)

porcentagem = (consumo * 0.25)

custo_total = (consumo + porcentagem)

print (round (custo_total, 2))