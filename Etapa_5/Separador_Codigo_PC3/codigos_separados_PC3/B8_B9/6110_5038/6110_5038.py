q = int(input("quantidade de combustivel: "))
if(q<17.5):
	total = q+10.5
	print(round(total,1))
elif(q>=17.5 and q<35.0):
	total = q + 14.0
	print(round(total,1))
elif(q>=35.0 and q<50.0):
	total = q+18.6
	print(round(total,1))
elif(q>=50):
	total = q+24.5
	print(round(total,1))
	