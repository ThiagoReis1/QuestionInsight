altura_macaco = 1.4
taxa_macaco = 0.06

a = float(input("altura: "))
t = float(input("taxa: "))

c = 0
v = altura_macaco + (taxa_macaco * c)

while (altura_macaco > a):
	if (t > taxa_macaco):
		c = c + 1
		
		a = float(input("altura: "))
		t = float(input("taxa: "))
print(c)

		
		