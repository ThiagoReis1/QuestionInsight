r=float(input(': '))
m=float(input(': '))
b=float(input(': '))
o=float(input(': '))
conta=(r*7+m*6+b*3+o*5)
if conta<=42:
	pagamento= conta-3
else:
	pagamento= conta-(0.10*conta)
t=(round(pagamento,2))
print (t," ", "ryous")