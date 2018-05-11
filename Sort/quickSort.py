def quickSort(a, s, l):
	if s < l:
		m = partion(a, s, l)
		quickSort(a, s, m-1)
		quickSort(a, m+1, l)

def partion(a, s, l):
	mid = a[l]
	i = s - 1
	for j in range(s, l):
		if a[j] <= mid:
			i = i + 1
			swap(a, i, j)
	swap(a, i+1, l)
	return i+1

def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

a = [5,7,3,2,6,8,0,1,9,4]
quickSort(a, 0, len(a)-1)

print(a)