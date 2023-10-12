def date_fashion(you, date):
  # you, 0-10
  # date, 0-10
  # int val, 0=no, 1=maybe, 2=yes
  # either of us 8 or more means 2yes
  # either of is 2 or less means 0no
  # else, 1maybe
  if you <= 2 or date <= 2:
    return 0 #no
  elif you >= 8 or date >= 8:
    return 2 #yes
  return 1 #maybe
