import itertools

def all_same(items):
    return all(x == items[0] for x in items)
#collection = [5 ,1 ,2 ,3 ,4 ,5]
n=int(raw_input())
line =  raw_input().split()
arr = [int(i) for i in line]
if all_same(arr):
	print len(arr)-1
	quit()
#dic = {1:[] , 2:[] , 3:[] , 4:[] , 5:[] , 6:[] , 7:[] , 8:[] , 9:[] }
pis = []

#for x in xrange(1,10):
#	elements = [i for i, j in enumerate(collection) if j == x]
#	#elements = dic[x]
	#print elements
#	if len(elements)>0:
		
#		for a, b in itertools.combinations(elements, 2):
#				if (b-a)%2!=0:
						#print "b-a : "+str(b-a)
						#print "adding to pis : <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>...."
						#print pis
#						if not a+((b-a)/2) in pis:
#							pis.append(a+((b-a)/2))
						#print pis
						#print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>...."

#print len(pis)
k=0
temp=0
f=False
temp_s=False
output=0
x=0
while x < len(arr):
	pis.append(arr[x])
	print pis
	print "x in this level : "+str(x)

	if x <= len(arr)-2 and arr[x] == arr[x+1]:
		if f == False:
			print "first double<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>."
			k=x
			f=True
			print "k : "+str(k)
			print f
			x+=1
			continue
			print "end<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,"
		else: 
			if temp_s == False:
				print "temp reserved<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>."
				temp=x
				temp_s=True
				print "TEMP : "+str(temp)

	if f == True:
		if pis[k] == arr[x]:
			k=k-1
			print "mines : "+str(k)
	
		else :
			f=False
			if temp_s == True:
				k=temp
				x=temp+1
				temp_s=False
				f=True
				print pis
				print "X : "+str(x)
				size = len(pis)
				for pp in xrange(x,size):
					print pp
					pis.pop()
				print "X : "+str(x)
				print pis
	if k == -1:
		if f == True:
			output=output+1
			f=False	
	print "k :"+str(k)
	print f
	x+=1

if f != False:
	output=output+1

print output