qi = int(input(" quantidade inicial "))
qc = int(input(" novos baloes construidos "))
qd = int(input(" baloes destruidos a cada semana "))
a = qi
t = 0
b = 200
while(a<200):
	a = a + (qc - qd) 
	t = t + 1
b = a - b
a = a - b
print(t)