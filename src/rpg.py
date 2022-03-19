import random

def roll(a,b):
  return random.randint(a,b)

def chancein(x):
  return roll(1,x)==1

def high(a,b):
  return max(roll(a,b),roll(a,b))

def low(a,b):
  return min(roll(a,b),roll(a,b))

def choose(choices,method=roll):
  return choices[method(0,len(choices)-1)]
