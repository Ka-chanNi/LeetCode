def quickSort(arg):
    if(arg == []):
        return []
    bigList = []
    smallList = []
    middle = arg[0]
    for i in arg[1:]:
        if i<=middle:
            smallList.append(i)
        else:
            bigList.append(i)
    return quickSort(smallList)+[middle]+quickSort(bigList)
print(quickSort([12,14,25,23,2,17,13,25,34,777]))