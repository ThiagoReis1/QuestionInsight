qddc = float(input())

if qddc < 17.5:
	c = qddc + 1.5
	print(round(c, 1))
	
elif qddc >= 17.5 and qddc <=35.0:
	c = qddc + 2.3
	print(round(c,1))
elif qddc >=35.0 and qddc <=50.0:
	c = qddc + 3.3
	print(round(c,1))
elif qddc >= 50:
	c = qddc + 4.7
	print(round(c,1))