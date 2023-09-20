def make_bricks(small, big, goal):
  # small brick val = 1
  # big brick val = 5
  # two strategies, use big bricks first, or use little bricks first
  # if make extra, that's fine too
  # little bricks or big bricks by themselves
  # what's my strategy?
    # bval = 5 # establish constants
    # sval = 1

    # 10 = 10 * 1
    # 9 = 10 * 1

    # take some big bricks
    # check if can be completed with small
    # if not, add another big brick, keep trying until no more big bricks, then return false
    bval = 5
    sval = 1

    # check if big bricks run out with mod, instead of using loop
    # 13 - 5 = 8 still bigger than 7
    # goal - big * bval <= small, return true
    
    if big != 0:
        mod = goal % bval
        # 13 % 5 = 3
        if small >= mod:
            # 7 >= 3
            return True
        sum = goal - big * bval
        if small >= sum:
            return True
        else:
            return False
    if goal <= sval * small:
        return True
    if goal <= bval * big:
        return True
    return False


if __name__ == '__main__':
    print(make_bricks(7, 1, 13), '7,1,13 --> False')