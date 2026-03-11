aj = 1.77
tj = 0.02

aa = input("Altura do aluno: ")
ta = input("TAxa de crescimento do aluno: ")

try :
	aa = float(aa)
	ta = float(ta)
	
except ValueError :
	print("Bah")
	
else :
	if ( aa <= 0 or ta <= 0) :
		print("Bah")
		
	else :
		t = 0
		while ( aa < aj ) :
			t += 1
			aa += ta
			aj += tj
		
		print(t)