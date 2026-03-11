alb = 1.69
tb = 0.01
tempo = 0
alp = float(input("altura de uma pessoa:"))
tc = float(input("taxa de crescimento:"))

while alp <=alb:
	alp = alp + tc
	alb = alb + tb
	tempo = tempo +1
print(tempo)