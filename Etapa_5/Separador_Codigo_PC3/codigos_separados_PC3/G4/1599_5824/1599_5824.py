from numpy import *
custo=array(eval(input("Vetor custo: ")))
ind=0
var=0
while ind<size(custo):
	
	if custo[ind]>=80.0:
		por=(15*custo[ind])/100
		var=var+por
		sum(custo)-var

	ind=ind+1
print(round(sum(custo)-var,2))
 