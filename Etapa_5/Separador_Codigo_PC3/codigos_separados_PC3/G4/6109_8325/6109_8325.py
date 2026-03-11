q=float(input("quantidade de combustivel: "))

if(q<=17.5):
	print(round(q+1.5,1))
elif((q>=17.5) and (q<=35)):
	print(round(q+2.3,1))
elif( (q>=35)and (q<=50)):
	print(round(q+3.3,1))
else:
	print(round(q+4.7,1))