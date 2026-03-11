#Universidade Federal do Amazonas
#Instituto de Ciencias Exatas e da Terra
#Oziel Ramos de Lima Junior
#21553853

valor = float(input())

custo_mes = 45.00
custo_minuto = 0.97*valor
total1 = custo_mes + custo_minuto 
total = total1 * 0.42
v = total + total1
print(round(v,2))

