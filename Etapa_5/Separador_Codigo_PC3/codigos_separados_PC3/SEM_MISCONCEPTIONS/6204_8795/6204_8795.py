altura_macaco = 1.86
taxa_macaco = 0.01
h=float(input())
t=float(input())
cont=0
while h<altura_macaco:
	altura_macaco=altura_macaco+taxa_macaco
	h=h+t
	cont=cont+1
print(cont)