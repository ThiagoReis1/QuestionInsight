n = input("n: ").upper()
w=0 
while(n!='S'):
	if(n!='ICOMP'):
		n=input("n:").upper()
	else:
		w=w+1
		n = input("n: ").upper()
		
print(w)