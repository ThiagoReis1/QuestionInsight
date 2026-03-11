altura_macaco = 1.86
taxa_macaco = 0.01
ac=float(input("Altura do coelho: "))
tc=float(input("Taxa de crescimento do coelho: "))
a=0

while ac<altura_macaco:
	a=a+1
	ac=ac+tc
	altura_macaco=altura_macaco+taxa_macaco
print(a)
