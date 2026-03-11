#----------------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# ANA REBECA CAVALCANTE EVANGELISTA
# MATRÍCULA: 21456290
# DATA: 16/06/2016
# OBJETIVO: Calcular o valor total a ser pago por determinada 
# encomenda
#-----------------------------------------------------------------

valor_encomenda = float(input("Qual o valor da encomenda?"))

imposto = ( valor_encomenda * (81/100) )
taxa = 12.00 

valor_total = (valor_encomenda + imposto + taxa)

print (round (valor_total, 2))