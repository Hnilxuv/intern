
def find_middle_two_arr(arr1, arr2):
    merge = []
    merge.extend(arr1)
    merge.extend(arr2)
    merge.sort()
    middle = float(len(merge))/2
    print(merge)
    if middle % 2 != 0:
        return merge[int(middle - .5)]
    else:
        return merge[int(middle - 1)]

if __name__ == "__main__":
    arr1 = [1, 2, 5, 7, 8]
    arr2 = [3, 4, 6]

    print(find_middle_two_arr(arr1, arr2))
