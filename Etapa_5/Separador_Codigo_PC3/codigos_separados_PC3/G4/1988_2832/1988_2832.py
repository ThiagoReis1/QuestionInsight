msg= input()
a=msg.upper() 

O=15.9994
C=12.011
N=14.00674
H=1.00794

if(a == "ARGININA"):
	print(round((C * 6) + (H *15) + (N *4) + ( O *2),2) )
elif(a== "TIROSINA"):
	print(round((C * 9) + (H *11) + (N) + ( O *3),2) )
elif(a=="TRIPTOFANO"):
	print(round((C * 11) + (H *11) + (N*2) + ( O *2),2) )
else:
	print("Entrada:",msg)
	print("Dado Invalido")