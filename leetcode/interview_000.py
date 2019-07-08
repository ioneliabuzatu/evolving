def solution(S, E):

    # all time ranges for each guest
    guests_time_range = {}

    for time_range in range(len(S)):
        arrive_leave = range(S[time_range], E[time_range])
        for each_guest in arrive_leave:
            guests_time_range[each_guest] = guests_time_range.get(each_guest, 0) + 1 # count how many guest are at each hour


    # get the maximum number of guest that is the max in the set of intersection of all ranges
    #return "The minimum number of chairs at the party is: " + str(max(set([value for key, value in guests_time_range.items()])))
    return max(guests_time_range.values())

S = [1,2,6,5,3]
E = [5,5,7,6,8]

print(solution(S,E))

