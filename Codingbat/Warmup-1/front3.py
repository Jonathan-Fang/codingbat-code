def front3(str):
  # front is first 3 chars of the string
  # if str len less than 3, front is the whole str
  if len(str) - 1 < 3:
    return str + str + str
  return str[0:3] + str[0:3] + str[0:3]
  # return 3 copies of the str
