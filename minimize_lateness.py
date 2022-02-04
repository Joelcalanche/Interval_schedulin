""""Problem Description
We are given n requests numbered 0 to n – 1. Each request i has a time that it takes to complete t(i) and a deadline d(i). If a request i starts at time s(i), then its finish time is f(i) = s(i) + t(i). The lateness of request i is L(i) = f(i) – d(i) if f(i) > d(i). The maximum value of L(i) over all i is called the maximum lateness. That is, maximum lateness = max(L(0), L(1), …, L(n – 1)). The problem is to schedule all the requests such that the value of maximum lateness is minimized."""


"""
Problem Solution
1. The function minimize_lateness defined.
2. It takes two lists ttimes and dtimes as arguments.
3. ttimes[i] is the time taken to complete request i.
4. dtimes[i] is the deadline of request i.
5. The algorithm works by sorting the requests in order of earliest deadline.
6. This ordering is an optimal way to schedule the requests to minimize maximum lateness.
7. The minimum maximum lateness is then calculated.
8. The minimum maximum lateness and the optimal schedule ordering is returned.

"""

"""
Program/Source Code
Here is the source code of a Python program to minimize maximum lateness using greedy algorithm. The program output is shown below.

"""



def minimize_lateness(ttimes, dtimes):
    """Return minimum max lateness and the schedule to obtain it.
 
    (min_lateness, schedule) is returned.
 
    Lateness of a request i is L(i) = finish time of i - deadline of if
    request i finishes after its deadline.
    The maximum lateness is the maximum value of L(i) over all i.
    min_lateness is the minimum value of the maximum lateness that can be
    achieved by optimally scheduling the requests.
 
    schedule is a list that contains the indexes of the requests ordered such
    that minimum maximum lateness is achieved.
 
    ttime[i] is the time taken to complete request i.
    dtime[i] is the deadline of request i.
    """
    # index = [0, 1, 2, ..., n - 1] for n requests
    index = list(range(len(dtimes)))
    # sort according to deadlines
    index.sort(key=lambda i: dtimes[i])
 
    min_lateness = 0
    start_time = 0
    for i in index:
        min_lateness = max(min_lateness,
                           (ttimes[i] + start_time) - dtimes[i])
        start_time += ttimes[i]
 
    return min_lateness, index




t1 = (0, 1, 8)

t2 = (1, 2, 7)

t3 = (2, 2, 10)

t4 = (3, 3, 4)

t5 = (4, 4, 8)

"""
orden correcto  minima latencia = t4=(3, 4),  t2= ( 2, 7), t1=(1, 8), t5=( 4, 8), t3=(2, 10); L=2 
indices ---------------------------3, 1,  0, 4, 2
"""



# print(t1[1:])



T = [t1, t2, t3, t4, t5]

T_ = [t[1:] for t in T]

for t in T:
    print(f"tarea{t[0]} con duracion {t[1]}, y deadline {t[2]}\n")

print("duracion")
ttimes = [t[1] for t in T]
print(ttimes)
print("deadline")
dtimes = [t[2] for t in T]
print(dtimes)



min_lateness, schedule = minimize_lateness(ttimes, dtimes)

print('The minimum maximum lateness:', min_lateness)
print('The order in which the requests should be scheduled (index):', schedule)


 
# n = int(input('Enter number of requests: '))
# ttimes = input('Enter the time taken to complete the {} request(s) in order: '
#               .format(n)).split()
# ttimes = [int(tt) for tt in ttimes]
# dtimes = input('Enter the deadlines of the {} request(s) in order: '
#                .format(n)).split()
# dtimes = [int(dt) for dt in dtimes]
 
# min_lateness, schedule = minimize_lateness(ttimes, dtimes)
