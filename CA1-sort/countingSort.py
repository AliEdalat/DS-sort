def countingSort(arr):

	n = len(arr)

	output = [0] * (n)

	count = [0] * (10)

	for i in range(0, n):
	
		count[ (arr[i])%10 ] += 1

	for i in range(1,10):
		count[i] += count[i-1]

	i = n-1
	while i>=0:
		
		output[ count[ (arr[i])%10 ] - 1] = arr[i]
		count[ (arr[i])%10 ] -= 1
		i -= 1

	i = 0
	for i in range(0,len(arr)):
		arr[i] = output[i]

n=int(raw_input())
line =  raw_input().split()
arr = [int(i) for i in line]
countingSort(arr)

for i in range(n):
	print ("%d" %arr[i]),