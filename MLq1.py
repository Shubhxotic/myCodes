import random,sys,numpy
p=dict()
for i in range(48,58):
	p[chr(i)]=0
print(p)
x=numpy.array([])
i=0
# for i in range(10000):
while(i<50000 or (i>50000 and (max(p.values())-min(p.values()))>500)):
	# y=[]
	# for j in range(10):
	temp=random.randint(10000,99999)
	for k in list(str(temp)):
		p[k]+=1
	# y.append(temp)
	# x.append(y)
	numpy.insert(x,0,temp)
	i+=1
print(max(p.values())-min(p.values()))
print(sys.getsizeof(x))
print(p)

su=sum(p.values())
print(su)
for i in p.keys():
	print("P(",i,") => ",p[i]/su)