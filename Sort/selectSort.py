def selectSort(a):
	for i in range(0, len(a)):
		minL = i
		for j in range(i, len(a)):
			if a[j] < a[minL]:
				minL = j
		temp = a[i]
		a[i] = a[minL]
		a[minL] = temp

a = [5,7,3,2,6,8,0,1,9,4,54,6,67,67,88,98,9,0,5,352]
selectSort(a)
print(a)