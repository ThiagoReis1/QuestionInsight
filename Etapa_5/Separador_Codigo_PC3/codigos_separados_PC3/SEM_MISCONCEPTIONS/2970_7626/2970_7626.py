tempo= int(input(""))
qf= 1000000 + 42000
q0= 1500.00
taxapt1= qf/q0
taxapt2= taxapt1 ** (1/tempo)
taxaf= taxapt2 - 1

print(round(taxaf, 5))

if taxaf <= 0.01:
	print("Real")
if taxaf > 0.01:
	print("Irreal")
