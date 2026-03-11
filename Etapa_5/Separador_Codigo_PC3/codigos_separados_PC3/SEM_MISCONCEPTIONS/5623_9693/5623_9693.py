menu= input("B ou S")
qtd_bs=int(input())
qtd_cap= int(input())
if menu == 'S':
	total=(qtd_bs*4.00)+(qtd_cap*7.50)
else:
	total=(qtd_bs*5.00)+(qtd_cap*7.50)
print(round(total,2))
