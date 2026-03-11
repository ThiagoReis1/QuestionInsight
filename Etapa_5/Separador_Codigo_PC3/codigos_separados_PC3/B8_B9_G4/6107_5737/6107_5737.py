qc = float(input("Quantidade de combustivel: "))

if(qc > 0):
	if(qc < 17.5):
		t = qc + 1.5
	elif(qc >= 17.5 and qc < 35):
		t = qc + 2.3
	elif(qc >= 35 and qc < 50):
		t = qc + 3.3
	elif(qc >= 50):
		t = qc + 4.7
	print(round(t,2))