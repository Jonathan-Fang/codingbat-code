def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  return False
  
""" # this doesn't work
monkey_trouble(a_smile, b_smile):
  if a_smile or b_smile:
    return False
  return True
"""
