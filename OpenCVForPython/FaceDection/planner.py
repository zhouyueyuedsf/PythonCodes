def planner(k):
	result = 1
	solution = [1]
	while(result < k):
		for s in solution:
			if (result + max(solution)) < 15:
				solution.append(result+max(solution))
				result += s
	print(solution)

planner(15)