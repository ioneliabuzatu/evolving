from itertools import permutations, combinations
import sys

def burger(distance_ingredients, repeat):

        output = {}
        totpermutations = permutations(distance_ingredients)
        value = 999999
        if len(distance_ingredients) > 4:
            for distance in totpermutations:
                value = min(value, (distance[0] - 0) ** 2 + (distance[1] - 1) ** 2 + sum(
                    [(i - 2) ** 2 for i in distance[2:-2]]) + (distance[-2] - 1) ** 2 + (distance[-1] - 0) ** 2)
        elif len(distance_ingredients) == 4:
            for distance in totpermutations:
                value = min(value, (distance[0] - 0) ** 2 + (distance[1] - 1) ** 2 + (distance[-2] - 1) ** 2 + (
                            distance[-1] - 0) ** 2)
        elif len(distance_ingredients) == 3:
            for distance in totpermutations:
                value = min(value, (distance[0] - 0) ** 2 + (distance[1] - 1) ** 2 + (distance[-1] - 0) ** 2)
        elif len(distance_ingredients) == 2:
            for distance in totpermutations:
                value = min(value, (distance[0] - 0) ** 2 + (distance[1] - 1) ** 2)
        else:
            if len(distance_ingredients) == 1:
                for distance in totpermutations:
                    value = min(value, (distance[0] - 0) ** 2)
        output[repeat] = "Case #{}: {}".format(repeat, value)
        print("Case #{}: {}".format(repeat, value))
        sys.stdout.flush()
    # return "\n".join(output.values())

# print(burger())


runs = int(input())
for repeat in range(1, runs + 1):
    ingredients = int(input())
    distance_ingredients = [int(x) for x in input().split()]
    burger(distance_ingredients, repeat)


