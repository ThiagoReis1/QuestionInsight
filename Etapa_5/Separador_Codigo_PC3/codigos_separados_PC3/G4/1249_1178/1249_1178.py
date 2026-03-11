from numpy import*
v= array(eval(input("Informe o vetor: ")))

for i in range(size(v)):
			x1 = round(int((0.7 * v[0] + 0.3 * v[9])-0.7000000000000002),0)
			x2 = round(int((0.4 * v[0] + 0.6 * v[9])-3.4000000000000004),0)
			z=[x1,x2]
			
print([z[0],z[1]])