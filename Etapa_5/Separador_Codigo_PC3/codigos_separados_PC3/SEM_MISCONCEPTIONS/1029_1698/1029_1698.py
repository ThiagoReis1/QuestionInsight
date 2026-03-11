#Marcos Felipe Melo de Lima	- 21554017
#Avaliação 01
#16/06/2016

chamadas = float(input("Qual foi o tempo de chamadas nesse mes? "))

custo_chamadas = 0.28 * chamadas
taxa_fixa = 23.0
custo_total = custo_chamadas + taxa_fixa 
custo_mes = (custo_total * 0.31) + custo_total

print(round(custo_mes, 2))
