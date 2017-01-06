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

"""Given an array of ints length 3, return the sum of all the elements.
sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7"""
def sum3(nums):
  sum = 0
  for i in nums:
      sum += i
  return sum

"""Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]"""
def rotate_left3(nums):
  return [nums[1],nums[2],nums[0]]
