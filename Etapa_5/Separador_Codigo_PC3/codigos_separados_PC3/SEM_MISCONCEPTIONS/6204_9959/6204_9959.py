altura_macaco = 1.86
taxa_macaco = 0.01

ac = float(input())
tc = float (input())

a = 0

while ac <= altura_macaco:
	altura_macaco += taxa_macaco
	ac += tc
	a += 1
	
print(a)