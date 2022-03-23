#!/usr/bin/python3
# Strategy wiki https://strategywiki.org/wiki/Castlevania:_Aria_of_Sorrow
#TODO with door-randomizer, make 2-way portals using teleporter rooms!
#TODO ideally the entrance door randomizer would put the player in a save room?
import progression,solver,items,shutil,rooms,args,spoilers,shop,rpg,monsters

AREAS=list(progression.areas.keys())
REWARDS=[progression.BACKDASH[0],progression.GLIDE[0],progression.JUMP[0],progression.SLIDE[0],progression.WATERWALK[0],progression.SINK[0],progression.FLIGHT[0]] #TODO can add good candidates 'Kicker skeleton','Hippogryph','Galamoth', "Black Panther' but is it too much for new players to realize they cleared an area? maybe if removed from elsewhere in the game, arule of "basic move = level cleared" could be a good guideline
FILLER=[progression.GLIDE[0],progression.WATERWALK[0],progression.SINK[0],progression.FLIGHT[0]] #TODO every area having a progression item would be essential for routing - this should be easy by placing duplicates of souls, as the game should allow it. (ideally would place multiple relics too, if game allows).
FILENAME=f'aros.{args.seed}'

rpg.setup()
while len(REWARDS)<len(AREAS):
  REWARDS.append(rpg.choose(FILLER,rpg.low))
s=None
while s==None or not s.solve():
  rewards={}
  rewardpool=list(REWARDS)
  for area in AREAS:
    i=rpg.low(0,len(rewardpool)-1)
    rewards[area]=rewardpool.pop(i)
  entrance=rpg.choose(AREAS,rpg.high)
  if rewards[entrance]==progression.FLIGHT[0]:
    continue
  s=solver.Solver(entrance,rewards)
with open(shutil.copy(args.rom,FILENAME+'.gba'),'r+b') as generated:
  with open(args.rom,'rb') as vanilla:
    monsters.load(vanilla)
    items.generate(rewards,vanilla,generated)
    rooms.generate(s,generated)
    shop.generate(generated)
spoilers.write(s,FILENAME)
