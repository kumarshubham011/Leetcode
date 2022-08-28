def even_odd(arr, left, right):
    if left >= right:
        return arr
    if arr[left] % 2 == 0:
        # means left ele is odd -> move left to next element
        return even_odd(arr, left + 1, right)
    elif arr[right] % 2 != 0:
        # right ele is odd - > decrement right to check prev ele
        return even_odd(arr, left, right - 1)
    else:
        # swap right and left
        arr[left], arr[right] = arr[right], arr[left]
        return even_odd(arr, left + 1, right - 1)


print(even_odd([4, 1, 3, 6, 5, 2, 7, 5, 5], 0, 8))
