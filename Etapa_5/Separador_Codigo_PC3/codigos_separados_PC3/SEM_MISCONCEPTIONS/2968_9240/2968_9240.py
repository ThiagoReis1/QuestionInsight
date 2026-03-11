salgadodequeijo = input("L ou S: ")
quantidade = int(input("quantidade: "))
guarana = int(input("guarana: "))

if salgadodequeijo == "L":
	print(quantidade * 5.00 + guarana * 4.00)
else:
	print(quantidade * 3.50 + guarana * 4.00)
	