qi = int(input("quantidade inicial"))
D1 = int(input("D1"))
D2 = int(input("D2"))
D3 = int(input("D3"))

N= (D1 + D2 + D3)
a= N * 10
S= (qi- a )


if(S == 0 or S < (-1) ):
	print("0")
	print("MORTO") 
else: 
	print(S)
	print("VIVO")
	
