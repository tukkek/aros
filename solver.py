#!/usr/bin/python3
import progression

VANILLAREWARDS={
  progression.CORRIDOR:progression.GLIDE[0],
  progression.STUDY:progression.JUMP[0],
  progression.HALL:progression.SLIDE[0],
  progression.QUARTERS:progression.WATERWALK[0],
  progression.TOWER:progression.SINK[0],
  progression.ARENA:progression.FLIGHT[0],
}

class Solver:
  def __init__(self,root,rewards):
    self.progress=set([root])
    self.actions=[f'Arrive at {root}.']
    
  def advance(self):
    advancement=False
    for a in progression.areas:
      if  a in self.progress:
        continue
      if progression.areas[a].enter(self):
        self.progress.add(a)
        self.actions.append(f'Can now enter: {a}!')
        advancement=True
    for r in VANILLAREWARDS:
      reward=VANILLAREWARDS[r]
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
