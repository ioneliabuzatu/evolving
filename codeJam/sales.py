def discounts():
    discount = {}
    rep = int(input())
    for repeat in range(1, rep + 1):
        out = []
        output = ""
        items = int(input())
        prices = [int(x) for x in input().split()]
        for i in prices:
            out.append(int(i - (0.25 * i)))
        for i in out:
            if i in prices:
                output = output + str(i) + " "
                # output.append(i)
                prices.remove(i)
        discount[repeat] = "Case #" + str(repeat) + ":" + " " + output
    return "\n".join(discount.values())

print(discounts(), flush=True)

# 2
# 3
# 15 20 60 75 80 100
# 4
# 9 9 12 12 12 15 16 20