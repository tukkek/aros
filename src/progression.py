#!/usr/bin/python3
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
BACKDASH=['Grave keeper']#not used in progression logic but have it here for uniformity's sake
FLIGHT=['Giant bat']
SINK=['Skula']#TODO can you sink as bat?
WATERWALK=['Undine']+FLIGHT
SLIDE=['Skeleton blitz'] #TODO can you "slide" through narrow passages as bat?
JUMP=['Malphas']+FLIGHT
GLIDE=['Flying armor']+FLIGHT#TODO is every glide solvable with jump?
#TODO Hippogryph

# save and teleporter rooms need to be considered for completion, as this offers most flexibility
class Solvable:
  def __init__(self,access=[],completion=[]):
    self.access=access#any valid entrance
    self.completion=completion#skill set to grab area's reward
  
  def enter(self,solver):#at least one met, in full
    for a in self.access:
      met=True
      for requirements in a:
        if not next((r for r in requirements if r in solver.progress),None):
          met=False
      if met:
        return True
    return False
  
  def complete(self,solver):#all met, at least one sub-item
    for requirements in self.completion:
      if not next((r for r in requirements if r in solver.progress),None):
        return False
    return True
  
  def __repr__(self):
    return f'access={self.access} completion={self.completion}'
  
teleporters={
  CORRIDOR:Solvable([[CORRIDOR]]),#would need jump to access from corridor itself
  CHAPEL:Solvable([[CHAPEL],JUMP]),
  HALL:Solvable([[HALL]]),
  QUARTERS:Solvable([[QUARTERS],WATERWALK]),#TODO also GLIDE/double JUMP?
  TOWER:Solvable([[TOWER],SINK]),
  RESERVOIR:Solvable([[RESERVOIR],SINK,FLIGHT]),#TODO confirm flight?
  ARENA:Solvable([[ARENA],JUMP]),#TODO seems reacheable without jump, maybe only glide?
  TOP:Solvable([[TOP],FLIGHT])
}

areas={
  CORRIDOR:Solvable(#TODO can you do the boss if you sequence-break?
    access=[teleporters[t].access for t in teleporters if t!=CORRIDOR]+
      [[[RESERVOIR],JUMP,SINK,GLIDE],#TODO test glide and single-jump. glide+jump from teleporter room?
       [[HALL],JUMP],
       [[GARDEN]],
       [[TOWER],SINK],
       [[CHAPEL]],#TODO assuming you don't need jump 
       [[QUARTERS],WATERWALK,JUMP]],#through top floor
    completion=[]),
  CHAPEL:Solvable(
    access=
      [[[CORRIDOR],GLIDE],
       [[STUDY],JUMP]], #TODO pretty sure jump is required
    completion=[JUMP]),
  STUDY:Solvable(access=[[[CHAPEL]]],completion=[]),
  HALL:Solvable(
    access=
      [[[CORRIDOR],GLIDE,JUMP],
       [[QUARTERS],SLIDE,JUMP]], #TODO coming from teleport, can you use less than jump?
    completion=[JUMP]), #TODO do you need jump to complete? can exit through TP rather than quarters
  QUARTERS:Solvable(
    access=#the top entrance is practically a corridor entrance, with the same requriements TODO confirm
      [[[HALL],JUMP,SLIDE],
       #[[CORRIDOR],GLIDE,JUMP],#TODO can left entrance be used with jump+glide?
       [[CORRIDOR],FLIGHT]],#top floor entrance (either, really)
    completion=[JUMP]),
  GARDEN:Solvable(
    access=
      [[[CORRIDOR],WATERWALK,JUMP],
       [[TOWER],JUMP,SINK]], #TODO from save im going to assume only jump but try less - from TP also sink, possibly WATERWALK?
    completion=[JUMP]),
  TOWER:Solvable(
    access=
      [[[GARDEN]],#TODO confirm no abilities required
       [[CORRIDOR],FLIGHT]],
    completion=[JUMP]), #TODO is jump required?
  RESERVOIR:Solvable(
    access=
      [[[CORRIDOR],SINK],
       [[ARENA],JUMP]],
    completion=[]),#no completion, just traversal? TODO
  ARENA:Solvable(
    access=[[[RESERVOIR],SINK,JUMP]],#TODO jump required?
    completion=[JUMP]),
  #TODO CEMETERY:Solvable(access=[],completion=[]),
  #TODO FORBIDDEN:Solvable(access=[],completion=[]),
  TOP:Solvable(#better to ignore lower room, treat it as Quarter-Corridor connection (elsewhere as well)
    access=#shortcut to tower is blocked from our side
      [[[QUARTERS],JUMP,WATERWALK,FLIGHT],
       [[CORRIDOR],FLIGHT]],#TODO confirm flight required
    completion=[FLIGHT]),
  #TODO CHAOS:Solvable(access=[],completion=[])
}
