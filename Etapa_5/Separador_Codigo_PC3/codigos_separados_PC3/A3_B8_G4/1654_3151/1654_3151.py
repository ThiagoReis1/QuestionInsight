from numpy import*
v=input("").split(',')
q=zeros(5,dtype=int)
AM=0
PE=0 
MG=0         
SP=0               
RS=0   
n=0
for x in v:
	if (x == "AM"):
   		AM=AM+1
        
	elif (x=="PE"):
   		PE=PE+1
        
	elif (x=="MG"):
   		MG=MG+1
        
	elif (x=="SP"):
   		SP=SP+1
        
	elif (x=="RS"):
   		RS=RS+1
	
        
q[0]=AM
q[1]=PE
q[2]=MG
q[3]=SP
q[4]=RS
print(max(q))
print(q)

	

