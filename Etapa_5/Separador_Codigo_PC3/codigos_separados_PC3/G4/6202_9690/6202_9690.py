ab = 1.69
tb = 0.01
A = float(input("altura: "))
T = float(input("taxa de crescaimento: "))
ano = 0

while ab>=A:
	A = A + T
	ab = ab + tb
	ano = ano + 1
print(ano)