altura_alice = 1.6
taxa_alice = 0.02

f = float(input())
t = float(input())

a = 0 

while (f < altura_alice) :
	altura_alice += taxa_alice
	f += t
	a += 1
print(a)