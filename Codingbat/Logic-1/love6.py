def love6(a, b):
  # if a or b is 6, return True
  # if a + b = 6 return True
  # if a - b = 6 return True
  if (a == 6 or b == 6) or (a + b == 6) or (a - b == 6) or (b - a == 6):
    return True
  return False
