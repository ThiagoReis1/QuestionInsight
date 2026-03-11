from math import*

dc=array(eval(input("combate: ").upper()))
nc=array(eval(input("nivel: ")))
i=0
ee=0

while(i<size(dc)):
	if(dc[i] == "CENOURA"):
		ee=dc[i]*2*nc
	elif(dc[i]== "FERRO"):
		ee=dc[i]*4*nc
	elif(dc[i]== "DWARVEN"):
		ee=dc[i]*8*nc
	elif(dc[i]=="ELVEN"):
		ee=dc[i]*11*dc[i]*nc
	elif(dc[i]=="DAEDRIC"):
		ee=dc[i]*14*nc
	i=i+1
print(ee)
	