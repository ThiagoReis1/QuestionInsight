#----------------------------------------------------------
#UNIVERSIDADE FEDERAL DO AMAZONAS
#VICTHORYA STHEFFANNY GOMES LIRA 
#DATA: 16/06/2016
#
#OBJETIVO: ESCREVER UM PROGRAMA QUE LEIA O PESO DA MERCADORIA 
#-----------------------------------------------------------
mercadoria=float(input("digite o peso da mercadoria "))
valor=43.21*mercadoria+25.0
imposto=valor*62%
Total=valor+imposto
print(float(total))