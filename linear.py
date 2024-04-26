
def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

list = [0,9,8,7,6,5]
target = 8

x = linear_search(list, target)
if x == -1:
    print(f"Target {target} not found")
else:
    print(f"Target {target} found")

