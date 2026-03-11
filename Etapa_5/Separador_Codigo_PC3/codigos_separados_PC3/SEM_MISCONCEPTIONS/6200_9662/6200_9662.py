altura_max = 1.75
taxa_max = 0.01
a = float(input("altura?")) #altura da pessoa 
t = float(input("taxa?"))  #taxa da pessoa
ano = 0
while a<altura_max:
	ano = ano + 1
	a = a+t
	altura_max = altura_max + taxa_max
print(ano)
