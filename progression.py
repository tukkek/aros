#!/usr/bin/python3
#TODO https://strategywiki.org/wiki/Castlevania:_Aria_of_Sorrow
#TODO with door-randomizer, make 2-way portals using teleporter rooms!
#TODO ideally the entrance door randomizer would put the player in a save room?
#TODO a full in-game review or accesses and completions would be a long-term goal
CORRIDOR='Castle corridor'
CHAPEL='Chapel'
STUDY='Study'
HALL='Dance hall'
QUARTERS='Inner quarters'
GARDEN='Floating garden'
TOWER='Clock tower'
RESERVOIR='Underground reservoir'
ARENA='The arena'
#TODO CEMETERY='Underground cemetery'
#TODO FORBIDDEN='Forbidden area'
TOP='Top floor'
#TODO CHAOS='Chaotic realm'

# making these Solvables would add to the complexity, let's try to in-line them where possible first
FLIGHT=['Giant bat']
SINK=['Skula']
WATERWALK=['Undine']+FLIGHT
SLIDE=['Skeleton blitz'] #TODO can you "slide" through narrow passages as bat?
JUMP=['Malapahas']+FLIGHT
GLIDE=['Flying armor']+FLIGHT#TODO is every glide solvable with jump?
#TODO Hippogryph

# save and teleporter rooms need to be considered for completion, as this offers most flexibility
class Solvable:
  def __init__(self,access=[],completion=[]):
    self.access=access#TODO at least one met, in full
    self.completion=completion#TODO all met, at least one sub-item
  
  def solve(progress):
    if len(access)>0:
      return False
    if len(completion)>0:
      return False
    return True
  
class Teleporter(Solvable):
  pass #TODO

class Area(Solvable):
  pass #TODO

teleporters={
  CORRIDOR:Teleporter([CORRIDOR]),#would need jump to access from corridor itself
  CHAPEL:Teleporter([CHAPEL],[JUMP]),
  HALL:Teleporter([HALL]),
  QUARTERS:Teleporter([QUARTERS],[WATERWALK]),#TODO also GLIDE/double JUMP?
  TOWER:Teleporter([TOWER],[SINK]),
  RESERVOIR:Teleporter([RESERVOIR],[SINK,FLIGHT]),#TODO confirm flight?
  ARENA:Teleporter([ARENA],[JUMP]),#TODO seems reacheable without jump, maybe only glide?
  TOP:Teleporter([TOP],[FLIGHT])
}

areas={
  CORRIDOR:Area(#TODO can you do the boss if you sequence-break?
    access=[teleporters[t] for t in teleporters if t!=CORRIDOR]+
      [[[RESERVOIR],JUMP,SINK,GLIDE],#TODO test glide and single-jump. glide+jump from teleporter room?
       [[HALL],JUMP],
       [[GARDEN]],
       [[TOWER],SINK],
       [[CHAPEL]]],#TODO assuming you don't need jump 
    completion=[GLIDE]),
  CHAPEL:Area(
    access=
      [[[CORRIDOR,GLIDE]],
       [[STUDY],JUMP]], #TODO pretty sure jump is required
    completion=[JUMP,GLIDE]),
  STUDY:Area(access=[[[CHAPEL]]],completion=[JUMP]),
  HALL:Area(
    access=
      [[[CORRIDOR],GLIDE],
       [[QUARTERS,SLIDE,JUMP]]], #TODO coming from teleport, can you use less than jump?
    completion=[JUMP]), #TODO do you need jump to complete? can exit through TP rather than quarters
  QUARTERS:Area(
    access=#the top entrance is practically a corridor entrance, with the same requriements TODO confirm
      [[[HALL],JUMP,SLIDE],
       [[CORRIDOR],GLIDE,FLIGHT]],#TODO can flight be replaced with jump+glide?
    completion=[JUMP,WATERWALK]),
  GARDEN:Area(
    access=
      [[[CORRIDOR],WATERWALK,JUMP],
       [[TOWER],JUMP,SINK]], #TODO from save im going to assume only jump but try less - from TP also sink, possibly WATERWALK?
    completion=[]),#TODO confirm it can be done without abilities
  TOWER:Area(
    access=
      [[[GARDEN]],#TODO confirm no abilities required
       [[TOP],FLIGHT], #from save just glide, if that
       [[CORRIDOR],FLIGHT]],
    completion=[]),
  RESERVOIR:Area(
    access=[],
    completion=[]),
  ARENA:Area(
    access=
      [[[CORRIDOR],SINK],#other corridor entrance requires jump as well
       [[ARENA],JUMP]], #from teleport just walk 
    completion=[]), #no completion, just traversal? TODO
  #TODO CEMETERY:Area(access=[],completion=[]),
  #TODO FORBIDDEN:Area(access=[],completion=[]),
  TOP:Area(
    access=#shortcut to tower is blocked from our side
      [[[QUARTERS],JUMP,WATERWALK],#from teleport just walk TODO confirm jump required
       [[CORRIDOR],FLIGHT]],#TODO confirm flight required
    completion=[]),
  #TODO CHAOS:Area(access=[],completion=[])
}
