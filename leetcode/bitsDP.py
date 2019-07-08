def bin(n):
    if n > 1:
        bin(n // 2)

    print(n % 2, end="")



def dpBits(n):
    out = []
    for number in range(n+1):
        count1 = 0
        while number >= 1:
            bit = number % 2
            if bit == 1: count1 += 1
            number = number // 2

        if count1: out.append(count1)
        else:
            out.append(0)

    return out



if __name__ == "__main__":
    print(dpBits(5))


