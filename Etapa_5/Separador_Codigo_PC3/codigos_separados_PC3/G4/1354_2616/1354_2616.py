pi = 3.1416
mw = int(input('Média em Watts desejada: '))
a = int(input('Raio do cômodo circular: '))
area = ((pi*a)**2)

print((area*mw)//1)