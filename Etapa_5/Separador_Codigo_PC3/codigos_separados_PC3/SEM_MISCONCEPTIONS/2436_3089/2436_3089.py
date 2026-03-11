from math import*
peso= float(input("qual o valor: "))
dis= float(input("qual o valor"))
peso1=peso*25.00
peso2=dis*0.10
icms=(peso1+peso2)*12/100
s=peso1+peso2+icms

print(round(s,2))
