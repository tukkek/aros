#!/usr/bin/python3
# Strategy wiki https://strategywiki.org/wiki/Castlevania:_Aria_of_Sorrow
#TODO with door-randomizer, make 2-way portals using teleporter rooms!
#TODO ideally the entrance door randomizer would put the player in a save room?
import progression,solver,items,shutil,rooms,args,spoilers,shop,rpg,monsters,rom

AREAS=list(progression.areas.keys())
REWARDS=[progression.BACKDASH[0],progression.GLIDE[0],progression.JUMP[0],progression.SLIDE[0],progression.WATERWALK[0],progression.SINK[0],progression.FLIGHT[0]] #TODO can add good candidates 'Kicker skeleton','Hippogryph','Galamoth', "Black Panther' but is it too much for new players to realize they cleared an area? maybe if removed from elsewhere in the game, arule of "basic move = level cleared" could be a good guideline
FILLER=[progression.GLIDE[0],progression.WATERWALK[0],progression.SINK[0],progression.FLIGHT[0]] #TODO every area having a progression item would be essential for routing - this should be easy by placing duplicates of souls, as the game should allow it. (ideally would place multiple relics too, if game allows).
FILENAME='aros' if args.debug else f'aros.{args.seed}'

rpg.setup()
while len(REWARDS)<len(AREAS):
  REWARDS.append(rpg.choose(FILLER,rpg.low))
s=None
while s==None or not s.solve():
  rewards={}
  pool=list(REWARDS)
  for area in reversed(AREAS):
    r=rpg.choose(pool,rpg.high)
    rewards[area]=r
    pool.remove(r)
  entrance=rpg.choose(AREAS)
  s=solver.Solver(entrance,rewards)
with open(args.rom,'rb') as vanilla:
  with open(shutil.copy(args.rom,FILENAME+'.gba'),'r+b') as generated:
    vanilla=rom.Rom(vanilla)
    generated=rom.Rom(generated)
    monsters.load(vanilla)
    items.generate(rewards,vanilla,generated)
    rooms.generate(s,generated)
    shop.generate(generated)
spoilers.write(s,FILENAME)
