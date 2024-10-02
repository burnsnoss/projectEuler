''' 
project euler problem 27 - burnsnoss - 09/10/2024

'''

import time
from util import eratosthenes, isPrime

def evaluateFunction(a, b, n):
  return (n ** 2) + (a * n) + b

if __name__ == '__main__':

  # find possible prime values for b
  possibleBs = eratosthenes(1000)
  possibleBs.pop(-1)

  # possible values of a
  possibleAs = range(-999, 1000)

  print('possible As and Bs generated')

  # try values of n in the function
  #  and test the result for primeness
  maximumN = 0
  AB = []
  for a in possibleAs:
    for b in possibleBs:
      n = 0
      while True:
        if not isPrime(evaluateFunction(a, b, n)):
          break
        n += 1

      if n > maximumN:
        maximumN = n
        AB = [a, b]
        print('NEW MAX - ', maximumN, AB)

  print('max N: ' + str(maximumN))
  print('[a, b]: ', AB)



  # just check that our answer is correct:
  # a = -61
  # b = 971

  # for n in range(0, 1012):
  #   print(evaluateFunction(a,b,n))

