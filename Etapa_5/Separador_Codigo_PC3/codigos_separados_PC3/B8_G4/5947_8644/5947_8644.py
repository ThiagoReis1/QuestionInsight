CE = input("C para coxinha ou E para esfirra: ")
x = int(input("quantidade de coxinhas ou esfirras: "))
y = int(input("quantidade de sucos: "))

c = 2.00
e = 4.50
s = 6.00

pc = (c*x) + (s*y)
pe = (e*x)+ (s*y)

if(CE == "C"):
	print(round(pc, 2))
else:
	if(CE >="E"):
		print(round(pe,2))