def alarm_clock(day, vacation):
  # return '7:00'
  # weekdays 1 - 5, alarm is 7:00
  # weekdays 1 <= day <= 5
  # weekend 0 and 6, alarm is 10:00
  # weekend 0 and 6
  # if vacation weekdays 10:00
  # if vacation weekends is off
  if vacation:
    if 1 <= day <= 5:
      return '10:00'
    else:
      return 'off'
  elif 1 <= day <= 5:
    return '7:00'
  return '10:00'
