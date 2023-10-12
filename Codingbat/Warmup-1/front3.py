def front3(str):
  # front is first 3 chars of the string
  # if str len less than 3, front is the whole str
  if len(str) - 1 < 3:
    return str + str + str
  return str[0:3] + str[0:3] + str[0:3]
  # return 3 copies of the str

# codingbat says
# def front_back(str):
#   if len(str) <= 1:
#     return str
  
#   mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
#   # last + mid + first
#   return str[len(str)-1] + mid + str[0]