#Universidade Federal do Amazonas 
#Laboratório de codificação 02
#PROVA
#Engenharia Química
#Pedro Vinícius Borges de Souza - 21650221

valor = int(input("dê um valor"))
a = valor // 1000
resto = valor % 1000
b = resto // 1000
b = resto% 1000
c = b // 1000

c = (( a + b) * (a + c) * (a+b) )


