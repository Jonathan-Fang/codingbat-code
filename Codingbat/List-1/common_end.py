# Prompt: Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
# Link: https://codingbat.com/prob/p147755
# Status: Solved October 12, 2023

def common_end(a, b):
  return (a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1])
