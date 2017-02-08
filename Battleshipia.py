from random import*
l=randint(1,10)
c=randint(1,10)
x=randint(1,10)
y=randint(1,10)
diffx=abs(x-l)
diffy=abs(y-c)
nbcoup=1
for ligne in range(1,11):
	for colonne in range(1,11):
		if l==ligne and c==colonne:
			while diffx!=0 and diffy!=0:
				print("retry")
				nbcoup=nbcoup+1
				if diffx==1 and diffy==1:
					print("en vue")
					diffx=x+1
					diffy=y+1
				else:
					print("a l'eau")
				x=randint(1,10)
				y=randint(1,10)
				diffx=abs(x-l)
				diffy=abs(y-c)
			else:
				print("coule en ligne",c,"colonne",l)
print("nbcoup=",nbcoup)
