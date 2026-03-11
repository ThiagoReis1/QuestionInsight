comb=int(input("quant de combustivel:" ))
if(comb<17.5):
	t= comb+1.5
elif(comb>=17.5) and (comb<35.0):
	t= comb+2.3
elif(comb>=35.0) and (comb<50.0):
	t=comb+3.3
elif(comb>=50.0):
	t=comb+4.7
print(round(t,1))