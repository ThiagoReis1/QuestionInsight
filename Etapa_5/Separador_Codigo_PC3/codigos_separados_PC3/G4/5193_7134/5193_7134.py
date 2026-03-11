ram = float(input("ramen:"))
men = float(input("menma:"))
bol = float(input("bolinho de arroz:"))
oni = float(input("onigi:"))
total = (ram*7.00) + (men*6.00) + (bol*3.00) + (oni*5.00)

if total <= 42:
	desc = total - 3
else:
	desc = total - ((total*10)/100)
print(round(desc, 2) , "ryous")