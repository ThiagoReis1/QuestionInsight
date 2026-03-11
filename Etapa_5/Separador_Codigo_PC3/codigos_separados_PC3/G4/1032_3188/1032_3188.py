#Encomendas tem um imposto de 81%
#Existe uma taxa fixa de 12,00

#Valor da encomenta (ve)
ve = float(input("Escreva o valor"))

#Valor do imposto (vi)
vi = 81 / 100

#Taxa fixa (tf)
tf = 12.00 

#Valor total a ser pago (vt)
vt = ve +(ve * vi) + tf

#Saida 
print(round(vt, 2))