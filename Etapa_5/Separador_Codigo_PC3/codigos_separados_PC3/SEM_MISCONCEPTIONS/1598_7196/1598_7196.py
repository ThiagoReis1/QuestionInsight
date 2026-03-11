from numpy import*

vcusto = array(eval(input("")))

i = 0

while i < size(vcusto):
	if vcusto[i] > 90:
		vcusto[i] = vcusto[i] - 6.5
	i = i + 1
print(round(sum(vcusto),2))