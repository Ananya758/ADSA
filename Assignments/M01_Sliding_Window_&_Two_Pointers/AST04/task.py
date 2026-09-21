def pairInSortedRotated(arr, target):
    n = len(arr)

    if n < 2:
        return False

    # Find the index of the smallest element
    min_index = 0
    for i in range(1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    # Left pointer at smallest element
    # Right pointer at largest element
    left = min_index
    right = (min_index - 1 + n) % n

    while left != right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True

        if current_sum < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n

    return False


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))
