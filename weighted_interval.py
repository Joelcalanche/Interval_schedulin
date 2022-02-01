import bisect # bisect recibe una lista ordenada y un numero y te indica el indice donde debes colocar el numero para que esta siga ordenada
# we want no know is which of all of these elemenst so what is the index of thesse of the element where the finish time is less than starting time

# le tenemos que restar 1 y nos dara el indice mas alto  donde no hay overlap
# this will find the P vector
def previous_intervals(I):
	p = []
	start = [task[0] for task in I]
	finish = [task[1] for task in I]


	for i in range(len(I)):
		idx = bisect.bisect(finish, start[i]) - 1

		p.append(idx)

	return p



# this is used for backtracking to find the optimal jobs 
def find_solution(j):
	# back tracking
	if j == -1:
		return

	else:
		if (I[j][2] + OPT[p[j]] >= OPT[j-1]):
			O.append(I[j])
			find_solution(p[j])

		else:
			find_solution(j-1)
#compute opt is to apply the recursive formula
def compute_opt(j):
	# Use recursive formula max(Wj + OPT(p(j)), OPT(j-1))
	# -1 en este caso rempleza al 0 de la explicaicion
	if j == -1:
		return 0 

	
	elif (0 <= j) and (j < len(OPT)):
		# cache
		return OPT[j]
	
	else:
		return max(I[j][2] + compute_opt(p[j]), compute_opt(j-1) ) 


# is to find the optimal for each of the subproblems, this is for a specific subset j and here will run this one for each for j =1 up to n
def weighted_interval(I):
	for j in range(len(I)):
		opt_j = compute_opt(j)
		OPT.append(opt_j)

	
	find_solution(len(I) - 1)
	return OPT[-1]




if __name__ == '__main__':
	# OPT for optimal weight, O for best items to pick

	OPT = [] # this store all of the optimal solution to all of the subproblems
	O = [] # store all of the best jobs to pick




	# They are labeled as: (start, end, weight)


	t1 = (0, 3, 3)

	t2 = (1, 4, 2)

	t3 = (0, 5, 4)

	t4 = (3, 6, 1)

	t5 = (4, 7, 2)

	t6 = (3, 9, 5)

	t7 = (5, 10, 2)

	t8 = (8, 10, 1)


	I = [t1, t2, t3, t4, t5, t6, t7, t8] # list of all of thouse tuples

	I.sort(key=lambda tup: tup[1])


	p = previous_intervals(I)

	opt_sol = weighted_interval(I)

	# print(opt_sol)

	print("maximun weight: " + str(opt_sol))

	print('The best jobs to take are' + str(O[::-1]))
