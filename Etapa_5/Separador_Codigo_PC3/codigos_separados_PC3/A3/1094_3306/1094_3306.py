#numero
numero= int(input("digite um numero de 6 digitos"))
#separar 1000
numero1= numero//1000
resto1= numero%1000
#separar de novo por 1000
numero2= resto1//1000
resto2= resto1%1000
#condição
cond= (numero1+resto2)**2
if(cond==numero):
	mensagem= "atende"
else:
	mensagem= "nao atende"
print(mensagem)
print(numero)