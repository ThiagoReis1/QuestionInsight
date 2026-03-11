from math import*
x = eval(input("Ângulo: "))
k = int(input("No. :"))

a = 0
b = 0
y=0
while y<k:
	a = a + ((-1)**(y))*((x**b)/(factorial(b)))
	y += 1 
	b +=2
print(round(a,10))