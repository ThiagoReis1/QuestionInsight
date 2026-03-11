ft = input()
qt = int(input())
cap = int(input())
if ft.upper() == "B":
   total=qt*5+cap*7.5
   print(round(total, 2))
else:
   total=qt*4+cap*7.5
   print(round(total, 2))