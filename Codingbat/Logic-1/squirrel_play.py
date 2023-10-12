def squirrel_play(temp, is_summer):
  # if 60 <= temp <= 90, play
  # if summer, 60<= temp <= 100, play
  if is_summer:
    if 60 <= temp <= 100:
      return True
    return False
  elif 60 <= temp <= 90:
    return True
  return False
