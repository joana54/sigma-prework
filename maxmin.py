def maxmin(arr):
    arr.sort()
    return [arr[0], arr[-1]]


if __name__ == "__main__":
    print(maxmin([2, 4, 1, 0, 2, -1]))
