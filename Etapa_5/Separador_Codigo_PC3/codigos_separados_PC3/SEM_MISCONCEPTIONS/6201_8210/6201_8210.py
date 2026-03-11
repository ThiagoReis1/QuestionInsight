altura_joe = 1.77
taxa_joe = 0.02
a = float(input("a: "))
t = float(input("t: "))
c=0

while altura_joe>a:
	altura_joe=altura_joe+taxa_joe
	a=a+t
	c=c+1
print(c)
