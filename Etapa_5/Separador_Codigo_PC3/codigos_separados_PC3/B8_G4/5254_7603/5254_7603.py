
p = float(input("preco do produto:"))
c = int(input("codigo da regiao"))

if c >=1 and c <=4:
	if c == 1:
		s = (( p -  p * 0.4) + p * ( 10 / 100))
	elif c == 2:
		s = ((p - ( p * 0.4)) + p * ( 8 / 100))
	elif c == 3:
		s = ((p - ( p * 0.4)) )
	elif c == 4:
		s = ((p - (p * 0.4)) + p * ( 2 / 100))
		
print(round(s, 2))

