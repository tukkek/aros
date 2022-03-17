import progression,rom

VANILLA={
  progression.CORRIDOR:progression.BACKDASH[0],#only one per area so ignore glide
  #progression.CHAPEL:,
  progression.STUDY:progression.JUMP[0],
  progression.HALL:progression.SLIDE[0],
  progression.QUARTERS:progression.WATERWALK[0],
  #progression.GARDEN:,
  progression.TOWER:progression.SINK[0],
  #progression.RESERVOIR:,
  progression.ARENA:progression.FLIGHT[0],
  #progression.TOP:)
}

class Item:
  def __init__(self,address):
    self.index=address#2 bytes
    self.category=self.index+2+2#2 bytes
    
  def replace(self,item,vanilla,generated):
    rom.copy(self.category,item.category,vanilla,generated)
    rom.copy(self.index,item.index,vanilla,generated)
    
shortsword=Item(0x510bf9),#first acessible item, for debugging
dash=Item(0x520bbd),#also useful for debugging

items={
  progression.BACKDASH[0]:Item(0x510c1d),
  progression.GLIDE[0]:Item(0x511145),
  progression.JUMP[0]:Item(0x513af1),
  progression.SLIDE[0]:Item(0x51554d),
  progression.WATERWALK[0]:Item(0x516d15),
  progression.SINK[0]:Item(0x519f7d),
  progression.FLIGHT[0]:Item(0x51f1d1),
}

def generate(rewards,vanilla,generated):
  for area in rewards:
    if area in VANILLA:#TODO
      items[rewards[area]].replace(items[VANILLA[area]],vanilla,generated)
