#!/usr/bin/python3
# Strategy wiki https://strategywiki.org/wiki/Castlevania:_Aria_of_Sorrow
#TODO with door-randomizer, make 2-way portals using teleporter rooms!
#TODO ideally the entrance door randomizer would put the player in a save room?
import progression,solver,random,items,shutil,doors,args,spoilers,shop

AREAS=list(progression.areas.keys())
REWARDS=[progression.BACKDASH[0],progression.GLIDE[0],progression.JUMP[0],progression.SLIDE[0],progression.WATERWALK[0],progression.SINK[0],progression.FLIGHT[0]] #TODO can add good candidates 'Kicker skeleton','Hippogryph','Galamoth', "Black Panther' but is it too much for new players to realize they cleared an area? maybe if removed from elsewhere in the game, arule of "basic move = level cleared" could be a good guideline
FILLER=[progression.GLIDE[0],progression.WATERWALK[0],progression.SINK[0],progression.FLIGHT[0]] #TODO every area having a progression item would be essential for routing - this should be easy by placing duplicates of souls, as the game should allow it. (ideally would place multiple relics too, if game allows).
SEED=args.seed  #TODO use as RNG seed, hash() if string
FILENAME=f'aros.{"debug" if args.debug else SEED}'#static filename helps with emulator saves for testing purposes

while len(REWARDS)<len(AREAS):
  a=random.randint(0,len(FILLER)-1)
  b=random.randint(0,len(FILLER)-1)
  REWARDS.append(FILLER[min(a,b)])
s=None
while s==None or not s.solve():
  rewards={}
  rewardpool=list(REWARDS)
  for area in AREAS:
    a=random.randint(0,len(rewardpool)-1)
    b=random.randint(0,len(rewardpool)-1)
    rewards[area]=rewardpool.pop(min(a,b))
  a=random.randint(0,len(AREAS)-1)
  b=random.randint(0,len(AREAS)-1)
  entrance=AREAS[max(a,b)]
  if rewards[entrance]==progression.FLIGHT[0]:
    continue
  s=solver.Solver(entrance,rewards)
with open(shutil.copy(args.rom,FILENAME+'.gba'),'r+b') as generated:
  with open(args.rom,'rb') as vanilla:
    items.generate(REWARDS,vanilla,generated)
    doors.generate(s,generated)
    shop.generate(generated)
spoilers.write(s,FILENAME)
