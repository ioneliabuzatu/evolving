def friendsTeather():
    out = {}
    for repeat in range(1, int(input()) + 1):
        counts = {}
        friends = []
        a = [int(x) for x in input().split()]

        for i in range(a[0]):
            print(i)
            friend = [int(x) for x in input().split()]
            friends.append(friend)

        stack = [friends[0]]

        for i in friends:
            if i != stack[0] and i != stack[0][::-1]:
                stack.append(i)

        for friend in stack:
            if len(set(friend)) == 1:
                del(friend[-1])
            for seat in friend:
                counts[seat] = counts.get(seat, 0) + 1
        out[repeat] = "Case #" + str(repeat) + ":" + " " + str(max(counts.values()))

    return "\n".join(out.values())


print(friendsTeather())

