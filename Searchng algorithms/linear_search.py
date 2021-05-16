def linear_search(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1

# test
print(linear_search([1,2,3,4,5,2,1], 2))