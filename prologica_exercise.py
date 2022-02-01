# if the starting time in j is >= finish time j-1, then mean is a viable next option, because then they don't overlap




def interval_scheduling(R,O):

	finish_time = 0

	for r in R:
		if finish_time <= r[0]:
			finish_time = r [1]
			O.append(r)





	return O


# request

r1 = (0, 3)

r2 = (1, 3)
r3 = (0, 5)

r4 = (3, 6)

r5 = (4, 7)

r6 = (3, 9)

r7 = (5, 10)

r8 = (8, 10)
r8 = (8, 10)


R = [r1, r2, r3, r4, r5, r6, r7, r8]
# We want to pick th earlist finish time first which mean that we have to sort it this list of tuples by the second element

R.sort(key=lambda x: x [1])

# Optimal solution

O = []
O = interval_scheduling(R, O)

print(O)