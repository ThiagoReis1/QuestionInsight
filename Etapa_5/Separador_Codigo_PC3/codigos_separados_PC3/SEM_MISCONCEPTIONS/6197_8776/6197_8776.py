altura_alice = 1.6
taxa_alice = 0.02
a = float(input())
b= float(input())
c = 0
while altura_alice > a:
	altura_alice = altura_alice + taxa_alice
	a = a + b
	c = 1 + c
print(c)