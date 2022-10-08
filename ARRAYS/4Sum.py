from ast import List

# METHOD 1: USING SORT AND BINARY SEARCH


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def binary_search(l, r, t):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == t:
                    return True
                elif nums[mid] > t:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        # using sort and binary search
        nums.sort()
        res = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    sm = nums[i] + nums[j] + nums[k]
                    t = target - sm
                    # perform binary search to find t in remaining array
                    found = binary_search(k+1, len(nums)-1, t)

                    if found:
                        res.append([nums[i], nums[j], nums[k], t])
        quad = []
        for n in res:
            if n not in quad:
                quad.append(n)
        return quad


# METHOD 2: USING SORTING AND 4 POINTERS
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # USING SORTING AND 4 POINTERS
        res = []
        nums.sort()

        for i in range(len(nums)):
            # remove duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                # remove duplicates
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                # use two sum to find other two pointers
                l, r = j+1, len(nums)-1
                while l < r:
                    sm = nums[i] + nums[j] + nums[l] + nums[r]
                    if sm == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        # removing duplicate l and r value
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l, r = l+1, r-1
                    elif sm > target:
                        r -= 1
                    else:
                        l += 1
        return res
