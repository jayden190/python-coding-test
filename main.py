from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    sub_sum = {0: 1}
    sum = 0
    count = 0
    for i, v in enumerate(nums):
        sum += v
        if sum - k in sub_sum:
            count += sub_sum[sum - k]
        if sum not in sub_sum:
            sub_sum[sum] = 0
        sub_sum[sum] += 1
    return count


nums = [[1,2],[3,4]]
nums[0].extend(nums[1])
print(sorted(nums[0]))