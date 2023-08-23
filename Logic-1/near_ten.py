def near_ten(num):
  # non-negative num
  # if num
  # multiples of 10
  # sample: 8 to 12; 18 to 20
  # n - 2 <= n <= n + 2
  # if n % 10 == 0, if n is a multiple of 10
  # if (n - 2) % 10 = 0
  # mod, 0,2,1,9,8; 01289
  # using lists here
  my_list = [0,1,2,8,9]
  if num % 10 in my_list:
    return True
  return False