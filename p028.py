''' 
project euler problem 28 - burnsnoss - 09/10/2024

'''

def evaluateDiagonalNumber(n, direction):
  if n == 0:
    return 1
  C = 0
  if direction == 'NE':
    return evaluateDiagonalNumber(n-1, 'NE') + (8 * n)
  if direction == 'NW':
    C = 6
  if direction == 'SW':
    C = 4
  if direction == 'SE':
    C = 2
  return evaluateDiagonalNumber(n - 1, direction) + (C + (8 * (n-1)))

if __name__ == '__main__':
  # n = RING NUMBER - calculated by taking side length s
  #  (s-1) / 2
  #
  #  e.g
  #  5x5 square is the 2nd RING around the origin point of 1
  #  (5-1) / 2 = 2
  #
  #  so for 1001x1001
  #  (1001 - 1) / 2 = 500
  nRange = range(1, 501)

  NElist = [1] * 501
  NWlist = [1] * 501
  SWlist = [1] * 501
  SElist = [1] * 501

  total = 1

  for n in nRange:
    NElist[n] = NElist[n-1] + (8*n)
    NWlist[n] = NWlist[n-1] + (6 + (8 * (n-1)))
    SWlist[n] = SWlist[n-1] + (4 + (8 * (n-1)))
    SElist[n] = SElist[n-1] + (2 + (8 * (n-1)))
    total += NElist[n] + NWlist[n] + SWlist[n] + SElist[n]

  print(total)
  

  



