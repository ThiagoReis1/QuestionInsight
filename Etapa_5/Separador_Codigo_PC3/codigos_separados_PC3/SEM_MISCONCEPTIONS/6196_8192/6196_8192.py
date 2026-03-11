altura_chico = 1.5
taxa_chico = 0.02

a = float(input("altura?: "))
t = float(input("taxa?: "))

cont = 0

while ( altura_chico > a ):
	altura_chico = altura_chico + taxa_chico 
	a = a + t 
	cont = cont + 1
print(cont)