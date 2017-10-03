def countingSort(arr,exp):
	size = len(arr)
	count = [0] * (10)
	output = [0] * (size)

	for x in xrange(0,size):
		index = (arr[x]/exp)
		count[index%10]+=1

	for z in xrange(1,10):
		count[z]+=count[z-1]
	
	i=len(arr)-1
	while i>=0:
		index = (arr[i]/exp)
		output[count[index%10]-1] = arr[i]
		count[index%10]-=1
		i-=1

	#copy output to arr

	for v in xrange(0,len(arr)):
		arr[v] = output[v]

def radixSort(arr):
	max_element = max(arr)
	exp = 1

	while (max_element/exp) > 0:
		countingSort(arr,exp)
		exp=exp*10

n=int(raw_input())
line =  raw_input().split()
arr = [int(i) for i in line]
radixSort(arr)

for i in range(len(arr)):
	print(arr[i]),
