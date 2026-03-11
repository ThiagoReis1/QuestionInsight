from numpy import*

n = array(eval(input("digite a nota: ")))
i = 0
p1 = 1
p2 = 2
p3 = 3
num =  n[0] * p1
num1 = n[1] * p2
num2 = n[2] * p3
s = num + num1 + num2
x = p1 + p2 + p3

print(round(s/x, 2))
		 
	
	