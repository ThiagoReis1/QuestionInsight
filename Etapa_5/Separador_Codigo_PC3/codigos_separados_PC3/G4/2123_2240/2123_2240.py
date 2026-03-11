from numpy import*
x = array(eval(input(""))) 
mf = sum(x)-min(x)
nf= mf/3
print(round(nf,2))
if nf >= 5:
	print("APROVOU")
else:
	print("REPROVOU")

	