q1 = int(input("qual a quantidade inicial na infataria?"))
q2 = int(input("qual a quantidade inicial na cavalaria?"))
p1 = float(input("qual o percentual da infantaria?"))
p2 = float(input("qual o percentual da cavalaria?"))

qt = 50000
m = 0

while ( qt >= q1 + q2 ):
	q1 = q1 + ( q1 * (p1/100))
	q2 = q2 + ( q2 * (p2/100))	
	m = m + 1
print(m)