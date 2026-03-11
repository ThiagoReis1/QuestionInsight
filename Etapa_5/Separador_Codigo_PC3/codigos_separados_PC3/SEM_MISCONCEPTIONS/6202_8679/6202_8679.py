altura_bia = 1.69
taxa_bia = 0.01

a = float(input())
t = float(input())
c = 0


while altura_bia > a:
	c = c + 1
	altura_bia += taxa_bia
	a += t 

print(c)