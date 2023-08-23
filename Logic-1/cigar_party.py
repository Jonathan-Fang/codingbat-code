def cigar_party(cigars, is_weekend):
  # if 40 <= cigars <= 60, then successful
  # if is_weekend, then cigars => 40
  # return False
  if is_weekend:
    if cigars >= 40:
      return True
  elif 40 <= cigars <= 60:
    return True
  return False
      
