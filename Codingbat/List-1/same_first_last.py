# Prompt: Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
# Link: https://codingbat.com/prob/p179078
# Status: Solved October 11, 2023

# Use Cases

def same_first_last(nums):
  # if array is 1 or more, and if first and last element are equal return true
  if nums != []:
    first = nums[0]
    last = nums[len(nums) - 1]
    if first == last:
        return True
    return False
  return False

# codingbat says
# return (len(nums) >= 1 and nums[0] == nums[-1])
# ITS SO CONCISE