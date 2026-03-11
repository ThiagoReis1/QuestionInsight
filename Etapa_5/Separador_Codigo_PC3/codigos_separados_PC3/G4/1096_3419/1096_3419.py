nf = int(input("numero forn: "))
n1 = (nf//10000)
n2 =(nf%10000)//100
n3 = (nf%100)

calc = n1**3 + n2**3 + n3**3

if (nf == calc):
	print("atende")
	print(calc)
else:
	print("nao atende")
	print(nf)