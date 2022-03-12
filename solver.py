#!/usr/bin/python3
import progression

class Solver:
  def __init__(self,root,rewards):
    self.progress=set([root])
    self.actions=[f'Arrive at {root}.']
    self.rewards=rewards
    
  def advance(self):
    advancement=False
    for a in progression.areas:
      if  a in self.progress:
        continue
      if progression.areas[a].enter(self):
        self.progress.add(a)
        self.actions.append(f'Can now enter: {a}!')
        advancement=True
    for r in self.rewards:
      reward=self.rewards[r]
      if not r in self.progress or reward in self.progress:
        continue
      if progression.areas[r].complete(self):
        self.progress.add(reward)
        self.actions.append(f'Acquired {reward} in {r}.')
        advancement=True
    return advancement
    
  def solve(self):
    while self.advance():
      continue
    return progression.FLIGHT[0] in self.progress
