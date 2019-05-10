kav=input()
c=0
for i in kav:
	if not( i.isalpha() or i.isdigit() or i==" "): 
		c+=1
print(c)
