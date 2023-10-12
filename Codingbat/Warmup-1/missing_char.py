def missing_char(str, n):
  # figure out how to remove a character in the first place
  # start with 1
  # find the pattern
  # return str[0:1] + str[2:]
  return str[0:n] + str[n + 1:]

# codingbat says
# def missing_char(str, n):
#   front = str[:n]   # up to but not including n
#   back = str[n+1:]  # n+1 through end of string
#   return front + back