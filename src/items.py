class Item:
  def __init__(self,address):
    #self.category=address+2+2+1+1#2 bytes
    #self.index=self.category+2+2#2 bytes
    self.index=address#2 bytes
    self.category=self.index+2+2#2 bytes
    
  def replace(self,item,vanilla,generated):
    copy(self.category,item.category,vanilla,generated)
    copy(self.index,item.index,vanilla,generated)

SHORTSWORD=Item(0x510bf9)#first acessible item, for debugging
FLYINGARMOR=Item(0x511145)
GRAVEKEEPER=Item(0x510c1d)

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
  FLYINGARMOR.replace(SHORTSWORD,vanilla,generated)
