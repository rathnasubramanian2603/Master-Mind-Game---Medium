import collections
import itertools
import random
import sys
import json
from random import shuffle
from ball import *
MAX_VALUE = 6
NUM_DIGITS = 4
NUM_TRIES = 6
NUM_TOTAL_POSSIBILITIES = MAX_VALUE ** NUM_DIGITS
_CODES = None
_COUNT = None
_POSSIBILITIES = None
best_guess=None 
class Game(object):
  def __init__(self):
    self.trialnum = 0
    self.codemaker()
    print('Code is',self.code)
  def getCode(self):
    return self.code
  def Reset(self):
    self.__init__()
  def codemaker(self):
    c=['b','c','d','e','f','g']
    shuffle(c)
    s=""
    for i in range(4):
        s=s+c[i]
    self.code=s
  def play(self,b):
    s=""
    for i in range(4):
        s=s+b[i].getcolor()
    return self.check(s)
  def check(self,s):
      black, white = ComputeProximity(s, self.code)
      self.trialnum += 1
      return black,white
          
def GetCount(code):
  global _COUNT
  if not _COUNT:
    _COUNT = {}
    for code_iterator in GetAllCodes():
      _COUNT[code_iterator] = [0] * MAX_VALUE
      for digit in code_iterator:
        _COUNT[code_iterator][int(ord(digit)-97) - 1] += 1
  return _COUNT[code]


def GetAllCodes():
  global _CODES
  if not _CODES:
    digits = [str(chr(i+97)) for i in range(1, MAX_VALUE + 1)]
    _CODES = sorted([''.join(list_digits) for list_digits in itertools.product(*([digits] * NUM_DIGITS))])
  return _CODES


def ComputeProximity(n, m):
  black = len([0 for d1, d2 in zip(n, m) if d1 == d2])
  count_n = GetCount(n)
  count_m = GetCount(m)
  black_and_white = sum([min(c1, c2) for c1, c2 in zip(count_n, count_m)])
  return black, black_and_white - black

