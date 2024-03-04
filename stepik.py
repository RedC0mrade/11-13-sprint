def zip_longest(*args, fill=None):
    lent = len(sorted(args, key=len)[-1])
    result = []
    for i in args:
        result.append(i + (lent-len(i))*[fill])
    return list(zip(*result))


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))