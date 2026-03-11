#Iranilson Prestes de Moraes
#Lab 1 Ex 1
#30/06/2016

a= float(input("valor da compra a "))
b= float(input("valor da compra b "))
c= float(input("valor da compra c "))
l= float(input("Limite do Cartao "))

Total = a + b + c
print (Total)

if Total <= l:
	mensagem ="sim"
else:
	mensagem ="nao"
	
print (mensagem)
	


