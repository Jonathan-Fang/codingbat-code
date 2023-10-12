def caught_speeding(speed, is_birthday):
  # 0 no tix
  # 1 small tix
  # 2 big tix
  # if speed <= 60, result is 0
  # if 61 <= speed <= 80, result is 1
  # if speed >= 81, result is 2
  # if birthday
  CONST = 5
  if is_birthday:
    if speed <= 60 + CONST:
      return 0
    elif 61 + CONST <= speed <= 80 + CONST:
      return 1
    elif speed >= 81 + CONST:
      return 2
  elif speed <= 60:
    return 0
  elif 61 <= speed <= 80:
    return 1
  elif speed >= 81:
    return 2
