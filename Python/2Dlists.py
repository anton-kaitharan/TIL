def sumArray(lists):
    if lists == []:
        return 0
    
    return lists[0] + sumArray(lists[1:])


list = [1, 2, 3, 4]
print(sumArray(list))

