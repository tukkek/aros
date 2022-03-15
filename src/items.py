import progression

class Item:
  def __init__(self,address):
    #self.category=address+2+2+1+1#2 bytes
    #self.index=self.category+2+2#2 bytes
    self.index=address#2 bytes
    self.category=self.index+2+2#2 bytes
    
  def replace(self,item,vanilla,generated):
    copy(self.category,item.category,vanilla,generated)
    copy(self.index,item.index,vanilla,generated)

items={
  'shortsword':Item(0x510bf9),#first acessible item, for debugging
  progression.BACKDASH[0]:Item(0x510c1d),
  progression.GLIDE[0]:Item(0x511145),
  progression.JUMP[0]:Item(0x513af1),
  progression.SLIDE[0]:Item(0x51554d),
  progression.WATERWALK[0]:Item(0x516d15),
  progression.SINK[0]:Item(0x519f7d),
  progression.FLIGHT[0]:Item(0x51f1d1)
}

def read(rom,at,length=2):
  rom.seek(at)
  return rom.read(length)

def write(value,at,to):
  to.seek(at)
  to.write(value)

def copy(a,b,vanilla,generated):
  p=read(vanilla,a)
  write(p,b,generated)

def generate(rewards,vanilla,generated):
  replace={
    #progression.FLIGHT[0]:progression.BACKDASH[0]
  }
  for r in replace:
    items[r].replace(items[replace[r]],vanilla,generated)
