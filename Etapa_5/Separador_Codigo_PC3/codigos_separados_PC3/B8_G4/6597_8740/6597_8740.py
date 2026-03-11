# faça seu código aqui!
n = int(input("numero de func: "))
c = 0
aa = 0
bb = 0
cc = 0
while c < n:
	num = input("tecnica").upper()
	if num == "A":
		c +=1
		aa +=1
	elif num == "B":
		c +=1
		bb += 1
	elif num == "C":
		c +=1
		cc += 1
print("A=", aa)
print("B=", bb)
print("C=", cc)