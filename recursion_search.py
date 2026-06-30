def recursion_search(lst, target):
    if len(lst) == 0:
        return False
    else :
        mid = (len(lst))//2
        if lst[mid] == target :
            return True
        else :
            if lst[mid] < target :
                return recursion_search(lst[mid + 1:], target)
            else :
                return recursion_search(lst[: mid], target)
            
def output_is(output):
    return f"tasget is {output}"
lsst = [1, 2, 3, 4, 5, 6, 7, 8, ]
output = recursion_search(lsst, 4)
print(output_is(output))