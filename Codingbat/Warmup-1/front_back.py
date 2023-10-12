def front_back(str):
  # find first char # str[0:1]
  # find last char # str[len(str) - 1:]
  # make new char and add
  # in between # str[1:-1]
  # str[-2:-1] + str[1:-1] + str[0:1]
  if len(str) == 1:
    return str
  return str[len(str) - 1:] + str[1:-1] + str[0:1]
  
# codingbat says
# def front_back(str):
#   if len(str) <= 1:
#     return str
  
#   mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
#   # last + mid + first
#   return str[len(str)-1] + mid + str[0]