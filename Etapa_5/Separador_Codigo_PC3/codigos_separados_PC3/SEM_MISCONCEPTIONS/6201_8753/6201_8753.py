a_joe = 1.77
t_joe = 0.02
ano = 0

altura = float(input("altura: "))
taxa = float(input("taxa: "))

while (altura < a_joe):
	a_joe = a_joe + t_joe
	altura = altura + taxa
	ano = ano + 1
print(ano)