def pos_neg(a, b, negative):
  if negative == True:
    if a < 0 and b < 0: # if both are negative, return true
      return True
    return False
  elif (a > 0 and b < 0) or (a < 0 and b > 0):
    return True
  return False
  
"""
  # return true if one is negative and one is positive
  if (a > 0 and b < 0) or (a < 0 and b > 0):
    return True
  # except if parameter "negative" is true
  elif negative == True:
    if a < 0 and b < 0:
      return True
    return False
  return False
"""