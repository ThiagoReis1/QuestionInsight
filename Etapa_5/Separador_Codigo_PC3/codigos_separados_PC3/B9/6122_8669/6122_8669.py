comum= float(input("combustivel comum: "))
if comum < 17.5:
	coax= 0.8
elif comum >= 17.5 and comum <= 35:
	coax= 1.3
elif comum >= 35 and comum <= 50:
	coax= 2.1
else:
	coax= 3

total= comum+coax
print(round(total,1))