altura_max = 1.75
taxa_max = 0.01
a = float(input())
b = float(input())
t = 0
while a< altura_max:
	a = a + b
	altura_max = altura_max + taxa_max
	t = t + 1
	
print(t)