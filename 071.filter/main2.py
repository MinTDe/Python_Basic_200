def getPrime(x):
    ret = [2]

    if x <= 2:
        return ret

    for i in range(3, x+1, 2):
        for j in range(3, int(i/2), 2):
            a = i % j
            if a == 0:
                break
        else:
            ret.append(i)

    return ret

ret = getPrime(10)
print(ret)
