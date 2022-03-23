import progression,rom,args,rpg,categories,monsters

LOOT=[0x5109dd,0x510af1,0x510afd,0x510bf9,0x510c11,0x510c1d,0x510dd9,0x510ed5,0x510f65,0x510fad,0x51103d,0x511145,0x5114c9,0x511565,0x511619,0x51163d,0x511715,0x511739,0x511769,0x51187d,0x51250d,0x5125cd,0x5125d9,0x512609,0x512615,0x512669,0x51271d,0x5127a1,0x5128f1,0x512939,0x5129c9,0x512a05,0x513875,0x5138f9,0x513911,0x513af1,0x513be1,0x513bf9,0x513c59,0x513c71,0x513d0d,0x513dfd,0x513ebd,0x51515d,0x5151a5,0x5152ad,0x5153f1,0x5154a5,0x51554d,0x5155d1,0x515781,0x516829,0x516835,0x51696d,0x516abd,0x516c9d,0x516d09,0x516d15,0x51714d,0x517d91,0x517e2d,0x517f1d,0x518175,0x518235,0x518301,0x5199d1,0x519cad,0x519f7d,0x51a0fd,0x51a3cd,0x51cbf5,0x51cd39,0x51cd5d,0x51ce05,0x51d015,0x51d051,0x51d1e9,0x51d32d,0x51d405,0x51d56d,0x51d801,0x51d825,0x51d8e5,0x51d981,0x51d999,0x51da7d,0x51dad1,0x51dc2d,0x51dc75,0x51dced,0x51dd29,0x51dd7d,0x51e25d,0x51e329,0x51f1d1,0x51f285,0x51f5fd,0x51f8b5,0x51f8e5,0x51f909,0x51f945,0x520bb1,0x520bbd,0x520bd5,0x520c35,0x520d6d,0x520e09,0x5211ed,0x521361,0x521385,0x521c5d,0x521d05,0x523cc1,0x523d99,0x523dbd,0x515a09,0x51d92d,0x51f4a1]
LOOTBYNAME={
  progression.GLIDE[0]:0x511145,
  progression.BACKDASH[0]:0x510c1d,
  progression.JUMP[0]:0x513af1,
  progression.SLIDE[0]:0x51554d,
  progression.WATERWALK[0]:0x516d15,
  progression.SINK[0]:0x519f7d,
  progression.FLIGHT[0]:0x51f1d1,
}
RELICS={
  progression.CORRIDOR:0x510c1d,#only one per area so ignore glide
  progression.CHAPEL:0x512609,
  progression.STUDY:0x513af1,
  progression.HALL:0x51554d,
  progression.QUARTERS:0x516d15,
  progression.GARDEN:0x518235,
  progression.TOWER:0x519f7d,
  progression.RESERVOIR:0x51cd5d,
  progression.ARENA:0x51f1d1,
  progression.TOP:0x521385
}
SELLPRICES={#from the wiki
  0x510c11:100,#cape 
  0x512609:25,#bamboo sword 
  0x516829:15000,#Dainslef 
  0x51cbf5:40,#pendant 
  0x51f5fd:1490,#black cloak 
  0x521c5d:50000#claimh solais 
}
BOOKS=[0x513d0d,0x516835,0x51da7d]
EXCLUDE=[26+i for i in range(6)] #books and maps
SHORTSWORD=0x510bf9#first acessible item from Corridor start, for testing
DASH=0x520bbd#black panther, for testing
EARLY=[0x510c11,SHORTSWORD,0x51cbf5]#couple rooms near the first Corridor safe, for testing
GOLD=[1,10,50,100,500,1000,2000]#$100 to $2,000 have been confirmed

class Loot:#an item in a room
  def __init__(self,address):
    self.address=address
    self.category=address+1#2 bytes
    self.index=self.category+2+2#2 bytes
    
  def replace(self,item,vanilla,generated):
    rom.copy(self.category,item.category,vanilla,generated)
    rom.copy(self.index,item.index,vanilla,generated)
    
  def __repr__(self):
    return f'({hex(self.address)} {self.index=} {self.category=})'
  
class Item:
  def __init__(self,category,address):
    self.category=category
    self.address=address
    self.indexaddress=address#2 bytes
    self.priceaddress=self.indexaddress+2+2#4 bytes
    
  def load(self,vanilla):#TODO
    self.index=rom.readint(self.indexaddress,vanilla)
    self.price=rom.readint(self.priceaddress,vanilla,4)
    
  def __repr__(self):
    return f'{self.index} ${self.price}'
  
  
loot={l:Loot(l) for l in LOOT}
armor={a.address:a for a in [Item(categories.ARMOR,0x5063b0+i*(2+2+4+3+1+2+1+5)) for i in range(45)]}
consumables={c.address:c for c in [Item(categories.CONSUMABLE,0x505b3c+i*(2+2+4+1+1+2+4)) for i in range(32)]}
weapons={w.address:w for w in [Item(categories.WEAPON,0x505d3c+i*(2+2+4+2+1+3+1+13)) for i in range(59)]}
items=[]

indexes={
  categories.ARMOR:list(armor.values()),
  categories.CONSUMABLE:list(consumables.values()),
  categories.WEAPON:list(weapons.values()),
}

def clear(generated):
  for l in loot:
    l=loot[l]
    rom.write(b'\x00\x00',l.index,generated)
    rom.write(b'\x01\x00',l.category,generated)

def appraise(category,index,loot,pool):
  top=pool[-1].price#this fallback can be problematic if player learn some fixed loot locations can be very powerful?
  if category==categories.GOLD:
    return GOLD[index]
  if loot.address in BOOKS:
    return top
  if loot.address in SELLPRICES:
    return SELLPRICES[loot.address]*2
  if category in categories.SOULS:
    category=monsters.BYSOUL[category-6]
    if index not in category:
      return top
    m=category[index]
    drops=[items[d].price for d in m.drops if d!=0]
    return top if len(drops)==0 else sum(drops)/len(drops)
  return indexes[category][index].price

def populate(vanilla,generated):
  pool=sorted((i for i in items if i.price>0 and not i.index in EXCLUDE),key=lambda x:x.price)
  for l in loot:
    if args.debug or rpg.chancein(3):
      l=loot[l]
      i=rom.readint(l.index,vanilla)
      category=rom.readint(l.category,vanilla)
      if category in categories.CANDLE:#TODO
        continue
      price=appraise(category,i,l,pool)
      if price==0:
        raise Exception('Unknown unpriced item',i,l)
      candidates=[c for c in pool if c.price<=price]
      if len(candidates)==0:
        continue
      c=rpg.choose(candidates,rpg.low)
      categoryindex=indexes[c.category]
      rom.writeint(categoryindex.index(c),l.index,generated)
      rom.writeint(c.category,l.category,generated)

def generate(rewards,vanilla,generated):
  for category in [consumables,weapons,armor]:
    for item in category:
      item=category[item]
      item.load(vanilla)
      items.append(item)
  clear(generated)
  populate(vanilla,generated)
  for area in rewards:
    l=loot[LOOTBYNAME[rewards[area]]]
    l.replace(loot[RELICS[area]],vanilla,generated)
