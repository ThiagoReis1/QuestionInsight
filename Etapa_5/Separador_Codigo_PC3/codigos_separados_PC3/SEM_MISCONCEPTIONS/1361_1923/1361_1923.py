from math import*
quantsnow=float(((5**(1/2))-1)/4)
quantsais=float((5-(2*(5**(1/2))))**(1/2))
quantaman=float(5*(5-(2*sqrt(5))))
quantidadedeporcoes=int(input("digite o numero de porcoes:"))
quant1=quantsnow*quantidadedeporcoes
quant2=quantsais*quantidadedeporcoes
quant3=quantaman*quantidadedeporcoes
print(round(quant1, 2))
print(round(quant2, 2))
print(round(quant3, 2))