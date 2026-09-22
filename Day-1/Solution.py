# Problem1: Function to rotate a list to the right by k position?
# Example: [1,2,3,4,5] --> [4,5,1,2,3]

nums = [1,2,3,4,5]
k = 0
def rotate_right(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

print(rotate_right(nums, k))