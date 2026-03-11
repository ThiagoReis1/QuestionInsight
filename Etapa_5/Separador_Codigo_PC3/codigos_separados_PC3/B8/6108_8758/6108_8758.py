cbs = int(input("quantidade de combudtivel: "))

if(cbs > 0) and (cbs < 17.5):
	total = cbs + 1.5
	print(round(total , 2))
	
elif(cbs >= 17.5) and (cbs < 35.0):
	total = cbs + 2.3
	print(round(total, 2))
	
elif(cbs >= 35.0) and (cbs < 50.0):
	total = cbs + 3.3
	print(round(total, 2))

elif(cbs >= 50.0):
	total = cbs + 4.7
	print(round(total, 2))