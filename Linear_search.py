def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target :
            return f"target {target} was at {i}th index"
    else :
        return f"target {target} was not found"
list1 = [11, 2, 1, 14, 5, 44, 63, 4]
print(linear_search(list1, 33))
