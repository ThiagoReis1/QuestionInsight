altura_luna = 1.65
taxa_luna = 0.02

f = float(input("altura da pessoa: "))
t = float(input("taxa de altura: "))

a = 0

while(f < altura_luna):
	altura_luna += taxa_luna
	f += t
	a += 1
print(a)
