alt= float(input("altura: "))
tax= float(input("taxa de crescimento: "))
altura_bia=1.69
taxa_bia=0.01
anos= 0
while(alt<altura_bia):
	altura_bia=altura_bia+taxa_bia
	alt=alt+tax
	anos=anos+1
print(anos)