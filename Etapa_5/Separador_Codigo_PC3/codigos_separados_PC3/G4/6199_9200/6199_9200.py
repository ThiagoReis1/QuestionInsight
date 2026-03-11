ac = 1.8
tc= 0.01

a = float(input("digite: "))
t = float(input("digite: "))
c = 0

while(ac > a):
	a = a + t
	ac = ac + tc
	c = c + 1
print(c)


