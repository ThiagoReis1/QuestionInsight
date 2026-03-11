#Custo de R$0,28 por minuto consumido
#Valor fixo de R$23,00 de assinatura
#31% de ICMS
#Escreva um programa que leia: o consumo de chamadas (em minutos) durante um certo mês
a = float(input("Chamada em minutos:"))
b = a * 0.28
c = b + 23
d = c + c*0.31
print(round(d, 2))