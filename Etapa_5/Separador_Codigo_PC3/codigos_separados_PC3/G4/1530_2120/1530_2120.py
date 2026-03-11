q1 = int(input("pergamos:"))
q2 = int(input("varas:"))
p1 = float(input("percentual1:"))
p2 = float(input("percentual2:"))

total = q2+q1
sto = 80000
tempo = 0

while(total<sto):
	q1 = (q1*p1)/100+q1
	q2 = (q2*p2)/100+q2
	tempo = tempo+1
	total = q2+q1
print(tempo)