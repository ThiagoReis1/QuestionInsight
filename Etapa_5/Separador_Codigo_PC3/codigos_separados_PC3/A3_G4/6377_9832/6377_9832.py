j = input("Digite o jogador que marcou: ").upper().split(",")

i = 0
tf = True
while ( i < len(j) ) :
	if (not j[i] in ["A","B","C","D"] ) :
		tf = False
		break
		
	i += 1
	
	
if ( tf ) :
	from numpy import *
	v0 = zeros(4, dtype = int)
	
	for i in j :
		if ( i == "A" ) :
			v0[0] +=1 
			
		elif ( i == "B" ) :
			v0[1] += 1
			
		elif ( i == "C" ) :
			v0[2] += 1
			
		else :
			v0[3] += 1
			
	print(v0)
	
else :
	print("A,B,C,D")