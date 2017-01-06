"""Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True"""
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False

"""Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
make_pi() → [3, 1, 4]"""
def make_pi():
  num = [3,1,4]
  return [num[0],num[1],num[2]]

"""Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True"""
def common_end(a, b):
  if a[0] == b[0]:
    return True
  if a[len(a)-1] == b[len(b)-1]:
    return True
  else:
    return False
