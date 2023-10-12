# Prompt: Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
# Link: https://codingbat.com/prob/p181624
# Status: Solved October 11, 2023
# Basic python list problems -- no loops.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.

def first_last6(nums):
    i = 0
    first = nums[0]
    if first == 6:
        # if first element is 6, return true
        return True
    # if last element is 6, return true
    last = nums[len(nums) - 1]
    if last == 6:
        return True
    for i in range(len(nums)): # turns out don't need the for loop, wait I can't use loops in this module
        i = i + 1
    return False
    # else return false