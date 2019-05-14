kavi=int(raw_input())
abhi=[]
for i in range(1, kavi + 1):
       if kavi % i == 0:
           abhi.append(i)
print(" ".join(str(n) for n in abhi))
