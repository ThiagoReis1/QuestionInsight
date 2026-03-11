#cumpom 35% de descont.
#uma viagem de ida e volta dentro do BR.
#cupom valido p/duas passagens aereas.
#desconto apenas p/o acompanhante.

v1=float(input("Informe o valor da passagem do cliente:"))
v2=float(input("informe o valor da passagem do acompanhante:"))

td=35/100 #taxa de desconto
d=v2-(v2*(35/100)) #desconto aplicado

#printar o valor total de cada passagem
print(round(v1, 2))
print(round(d, 2))
print(round(v1+d, 2))

