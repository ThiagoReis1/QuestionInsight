a = float(input())
t = float(input())
ac = 1.75
tc = 0.01
anos = 0
while ac>a:
   a = a + t
   ac = ac + tc
   anos = anos + 1
print(anos)