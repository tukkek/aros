#!/usr/bin/python3
import progression,random

class Solver:
  def __init__(self,root,rewards):
    self.progress=set([root])
    self.actions=[f'Arrive at {root}.']
    self.rewards=rewards
  
  def done(self):
    f=progression.FLIGHT[0]
    t=progression.TOP
    return f in self.progress and t in self.progress
  
  def advance(self):
    advancement=False
    for r in self.rewards:
      reward=self.rewards[r]
      if not r in self.progress or reward in self.progress:
        continue
      if progression.areas[r].complete(self):
        self.progress.add(reward)
        self.actions.append(f'Acquired {reward} in {r}.')
        advancement=True
        if reward==progression.FLIGHT[0] and self.done():
          self.actions.append('Done.')
    for a in progression.areas:
      if a in self.progress:
        continue
      if progression.areas[a].enter(self):
        self.progress.add(a)
        self.actions.append(f'Can now enter: {a}!')
        advancement=True
        if a==progression.TOP and self.done():
          self.actions.append('Done.')
    return advancement
    
  def solve(self):
    while self.advance():
      continue
    return self.done()
