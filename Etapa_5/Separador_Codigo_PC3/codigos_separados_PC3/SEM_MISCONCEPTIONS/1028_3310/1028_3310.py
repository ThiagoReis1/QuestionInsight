#Instituto de Computacao - UFAM
#Lab 02
#02/04/2018

#conta de agua custa 0,37 p/m**3
# (+) vf 15 = taxa de tratamento de esgoto
# total = 35% de ICMS 

#LEIA: volume de agua consumida 
volume = float(input("Digite o volume: "))

#conta
total = ((0.37 * volume) + 15)

#imposto
icms = ((total * 35)/100)
valor = icms + total

#saida: valor a ser pago
print(round(valor,2))
