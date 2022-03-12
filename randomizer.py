#!/usr/bin/python3
import progression,solver,random

VANILLAREWARDS={
  progression.CORRIDOR:progression.GLIDE[0],
  progression.STUDY:progression.JUMP[0],
  progression.HALL:progression.SLIDE[0],
  progression.QUARTERS:progression.WATERWALK[0],
  progression.TOWER:progression.SINK[0],
  progression.ARENA:progression.FLIGHT[0],
}
AREAS=[progression.CORRIDOR,progression.STUDY,progression.HALL,progression.QUARTERS,progression.TOWER,progression.ARENA]
REWARDS=[progression.GLIDE[0],progression.JUMP[0],progression.SLIDE[0],progression.WATERWALK[0],progression.SINK[0],progression.FLIGHT[0]]

s=None
#i=1
while s==None or not s.solve():
  #print(f'Generating #{i}...')
  #i+=1
  milestones={}
  rewards=list(REWARDS)
  for area in AREAS:
    a=random.randint(0,len(rewards)-1)
    b=random.randint(0,len(rewards)-1)
    milestones[area]=rewards.pop(min(a,b))
  s=solver.Solver(progression.CORRIDOR,milestones)
print('Log:')
for a in s.actions:
  print('- '+a)
