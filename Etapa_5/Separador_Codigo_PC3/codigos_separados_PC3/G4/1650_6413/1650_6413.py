from numpy import*

st = input("String: ")
m = 0
#print(m)
#vet = array(eval(input("Quantidade de clientes: ")))

for st in st:
	if(st.split(',') == "P" or st.split(',') == "C" or st.split(',') == "R" or st.split (',') == "L" or st.split(',') == "B"):
		m = m + st
print(m)