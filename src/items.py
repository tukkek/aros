import progression,rom,args

ITEMS={}

class Item:
  def __init__(self,name,address):
    self.name=name.lower()
    self.index=address#2 bytes
    self.category=self.index+2+2#2 bytes
    ITEMS[self.name]=self
    
  def replace(self,item,vanilla,generated):
    rom.copy(self.category,item.category,vanilla,generated)
    rom.copy(self.index,item.index,vanilla,generated)

helpers=args.debug and [#useful for debugging
  Item('short sword',0x510bf9),#first acessible item from Corridor start
  Item('black panther',0x520bbd),#dash
]

glide=Item(progression.GLIDE[0],0x511145)#TODO needs to be removed from map too after randomization

placement={
  progression.CORRIDOR:Item(progression.BACKDASH[0],0x510c1d),#only one per area so ignore glide
  progression.CHAPEL:Item('Bamboo Sword',0x512609),
  progression.STUDY:Item(progression.JUMP[0],0x513af1),
  progression.HALL:Item(progression.SLIDE[0],0x51554d),
  progression.QUARTERS:Item(progression.WATERWALK[0],0x516d15),
  progression.GARDEN:Item('$500',0x518235),
  progression.TOWER:Item(progression.SINK[0],0x519f7d),
  progression.RESERVOIR:Item('elfin robe',0x51cd5d),
  progression.ARENA:Item(progression.FLIGHT[0],0x51f1d1),
  progression.TOP:Item('Kaladbolg',0x521385)
}

def generate(rewards,vanilla,generated):
  for area in rewards:
    ITEMS[rewards[area].lower()].replace(placement[area],vanilla,generated)
