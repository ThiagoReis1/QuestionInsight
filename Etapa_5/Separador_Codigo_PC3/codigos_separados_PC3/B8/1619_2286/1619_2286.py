from numpy import*
t = array(eval(input("")))
m = array(eval(input("")))
m[0] == t[0]
m[1] == t[1]
m[2] == t[2]
m[3] == t[3]
if(m[0] == "QUENTE"):
	custo = 0.005*90*t[0]+ sum(t)
elif(m[0] == "MORNO"):
	custo = 0.005*45*t[0]+ sum(t)
elif(m[0] == "FRIO"):
	custo = 0.005*0*t[0]+ sum(t)
elif(m[1] == "QUENTE"):
	custo = 0.005*90*t[1]+ sum(t)
elif(m[1] == "MORNO"):
	custo = 0.005*45*t[1]+ sum(t)
elif(m[1] == "FRIO"):
	custo = 0.005*0*t[1]+ sum(t)
elif(m[2] == "QUENTE"):
	custo = 0.005*90*t[2]+ sum(t)
elif(m[2] == "MORNO"):
	custo = 0.005*45*t[2]+ sum(t)
elif(m[2] == "FRIO"):
	custo = 0.005*0*t[2]+ sum(t)
elif(m[3] == "QUENTE"):
	custo = 0.005*90*t[3]+ sum(t)
elif(m[3] == "MORNO"):
	custo = 0.005*45*t[3]	
elif(m[3] == "FRIO"):
	custo = 0.005*0*t[3]	
elif(m[4] == "QUENTE"):
	custo = 0.005*90*t[4]
elif(m[4] == "MORNO"):
	custo = 0.005*45*t[4]
elif(m[4] == "FRIO"):
	custo = 0.005*0*t[4] 
print (round(custo , 2))	
			