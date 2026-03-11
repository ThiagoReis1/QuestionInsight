qd = float(input("quantidade de combustivel: "))

if qd < 17.5 :
	total = qd + 1.5
	print(round(total, 1))


elif (17.5 <= qd) and (qd < 35) :
	total = qd + 2.3
	print(round(total, 1))
	
elif (35 <= qd) and (qd < 50) :
	total = qd + 3.3
	print(round(total, 1))
	
elif qd >= 50 :
	total = qd + 4.7
	print(round(total, 1))
