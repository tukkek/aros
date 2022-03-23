BYSOUL={category:{} for category in range(0,3+1)}

class Monster:
  def __init__(self,address):
    self.address=address
    common=address+8
    rare=common+2
    self.drops=[common,rare]
    self.hp=rare+2
    self.mp=self.hp+2
    self.xp=self.mp+2
    self.attack=self.xp+2+2
    self.defense=self.attack+1
    category=self.defense+1+1
    index=category+1
    self.soul=[index,category]
    
  def load(self,vanilla):
    self.drops=[vanilla.readint(d) for d in self.drops]
    self.hp=vanilla.readint(self.hp)
    self.mp=vanilla.readint(self.mp)
    self.xp=vanilla.readint(self.xp)
    self.attack=vanilla.readint(self.attack,1)
    self.defense=vanilla.readint(self.defense,1)
    self.soul=[vanilla.readint(s,1) for s in self.soul]
    
monsters=[Monster(0xe9644+i*36) for i in range(113)]

def load(vanilla):
  for m in monsters:
    #print(hex(m.address),hex(m.soul[0]),hex(m.soul[1]))
    m.load(vanilla)
    BYSOUL[m.soul[1]][m.soul[0]]=m
    #print(hex(m.address),m.soul)
