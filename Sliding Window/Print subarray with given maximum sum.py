# SLIDING WINDOW APPROACH

def sub_with_giv_sum(arr, k):
    start = 0
    curr_sum = 0
    res = []
    for end in range(0, len(arr)):
        curr_sum += arr[end]
        if curr_sum > k:
            # we will shift start pointer by one and subtract start element from sum
            curr_sum -= arr[start]
            start += 1
        if curr_sum == k:
            # print the subarray
            temp = []
            for i in range(start, end + 1):
                temp.append(arr[i])
            res.append(temp)
    return res if len(res) > 0 else -1


r = sub_with_giv_sum([1, 9, 3, 7], 10)
print(r)
r = sub_with_giv_sum([1, 8, 3, 20], 10)
print(r)


# Create two variables, start=0, currentSum = arr[0]
# Traverse the array from index 0 to end.
# Update the variable currentSum by adding current element, currentSum = currentSum + arr[i]
# If the currentSum is greater than the given sum, update the variable currentSum as currentSum = currentSum – arr[start],
# and update start as, start++.
# If the currentSum is equal to given sum, print the subarray.
