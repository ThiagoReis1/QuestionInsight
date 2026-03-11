altura_alice = 1.6
taxa_alice = 0.02
a = float(input())
t = float(input())
cont = 0

while (a <= altura_alice):
	a = float(input())
	cont += 1
	if (t != taxa_alice):
		t = int(input())
	cont += 1
	
n = a*t
print(n)

