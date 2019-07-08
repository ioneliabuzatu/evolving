from collections import deque, defaultdict



# class Itinerary:

#    def findit(self, ticks, start):

        # output = []
        # output.append(start)
        # while len(output) < len(ticks)+1:
        #     for trip in ticks:
        #         if start in trip:
        #             output.append(trip[1])
        #             start = trip[1]
        #
        # return output

# sol = Itinerary()
# print(sol.findit([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], "JFK"))
# # [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]


# numbers = [input() for num in range(int(input()))]
# print(numbers)

# n = ['07895462130', '919875641230', '9195969878']

# print(["+91" + " " + num[-10:-5] + " " + num[-5:] for num in n])

# # decorator
# def wrapper(f):
#     def stripping(listing):
#         f(["+91" + " " + num[-10:-5] + " " + num[-5:] for num in listing])
#
#     return stripping
#
#
#
# # sorting
# @wrapper
# def phone_numbers(listing):
#     print(*sorted(listing), sep="\n")
#
# phone_numbers(n)
#


# def appending_to(*number, to=[]):
#     to.append(number)
#     return to
#
# # appending_to(1)
# print(appending_to(2, 4))

# nei = None

# class Solution:
#     def networkDelayTime(self, times, K=None):
#         """
#         :type times: List[List[int]]
#         :type N: int
#         :type K: int
#         :rtype: int
#         """
#         global nei
#
#         graph = defaultdict()
#         delay = 0
#
#         for time in times:
#             departure, target, weight = time
#             if departure not in graph:
#                 graph[departure] = []
#             graph[time[0]].append((target, weight))
#
#         if K in graph.keys():
#             for tup in range(len(graph[K])):
#                 nei = graph[K][tup][0]
#                 delay += graph[K][tup][1]
#             if nei in graph.keys():
#                 value_neighbour = graph[nei]
#                 for tup_neighbour in range(len(graph[nei])):
#                      # print(graph[nei])
#                      delay += graph[nei][tup_neighbour][1]
#
#         return graph, delay
#
# g = [[1,2,1],[2,3,2]]
#
# sol = Solution()
# print(sol.networkDelayTime(g, 1))


# class DirectedGraph:
#
#     def __init__(self):
#         self.graph = defaultdict()
#         self.count = 0
#
#     # adding vertices and edges
#     # adding the weight is optional
#     # handels repetition
#
#     def rooms_add(self, rooms):
#
#         for room in range(len(rooms)):
#             if room not in self.graph:
#                 self.graph[room] = rooms[room]
#             #     keys = rooms[room]
#             # self.graph[room].append(keys)
#
#
#     def add_edge(self, u, v, w=None):
#         if self.graph.get(u):
#             if self.graph[u].count([w, v]) == 0:
#                 self.graph[u].append([v])
#         else:
#             self.graph[u] = [v]
#         if not self.graph.get(v):
#             self.graph[v] = []
#
#     def all_nodes(self):
#         # return list(self.graph)
#         return self.graph
#
#     def dfs(self):
#         stack = list(self.graph)[::-1]
#         assert type(stack) == list
#
#         while stack:
#             root = stack.pop()
#             print(self.graph[root])
#             for val in self.graph[root]:
#                 if val in self.graph.keys():
#                     self.count += 1
#
#         if self.count == len(self.graph)-1:
#             return True
#         else:
#             return False

class Solution:

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict()
        count = 0
        set_values = []

        for room in range(len(rooms)):
            if room not in graph:
                graph[room] = rooms[room]

        stack = list(graph)[::-1]

        assert type(stack) == list

        print(graph)

        while stack:
            root = stack.pop()
            if root+1 in graph[root]:
                set_values.append(root+1)

        return len(set_values)+1 == len(graph.keys())


input1=[[1],[2],[3],[]]
input2 = [[1],[2],[],[3]]
sol = Solution()
print(sol.canVisitAllRooms(input2))

