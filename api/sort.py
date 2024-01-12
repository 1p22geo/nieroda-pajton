def fnsort(data, fun):
    if len(data) == 0:
        return []
    if len(data) == 1:
        return data
    if len(data) == 2:
        if fun(data[0]) > fun(data[1]):
            return [data[1], data[0]]
        else:
            return [data[0], data[1]]
    pivot = data[0]
    ar1 = []
    ar2 = []
    for elem in data[1:]:
        if fun(elem) > fun(pivot):
            ar2.append(elem)
        else:
            ar1.append(elem)
    arr = []
    arr.extend(fnsort(ar1, fun))
    arr.append(pivot)
    arr.extend(fnsort(ar2, fun))

    return arr
