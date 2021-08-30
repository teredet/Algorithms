def binary_search(lys, val):
    '''
    lys - list in which to search
    val - value to find
    '''
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

if __name__ == "__main__":
    print(binary_search([1,2,3,4,5,2,1], 2))