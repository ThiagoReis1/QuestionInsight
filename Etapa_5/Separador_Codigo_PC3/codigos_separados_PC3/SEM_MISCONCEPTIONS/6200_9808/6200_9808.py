
altura = float(input("qual a altura: "))
cresc = float(input("qual o cresc: "))

altura_max = 1.75
taxa_max = 0.01

cont = 0

while (altura < altura_max):
	altura = altura + cresc
	altura_max = altura_max + taxa_max
	cont = cont + 1
	
print (cont)
