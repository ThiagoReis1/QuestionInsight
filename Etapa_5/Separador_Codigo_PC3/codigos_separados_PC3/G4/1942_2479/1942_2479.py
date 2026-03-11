amino = str(input("Histidina ou Prolina? "))

O=15.999
C=12.011
N=14.00674
H=1.00794
	
his = (C*6)+(H*10)+(N*3)+(O*2)
pro = (C*5)+(H*10)+(N)+(O*2)

if (amino.lower() == "histidina"):
	print(round(his, 2))
	
else:
	print(round(pro, 2))