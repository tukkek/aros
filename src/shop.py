STARTINGSOUL=[0x0]*2
#TODO assuming this is the memory override, we could maybe start without any items - might be interesting if not prohibibite for later area spawns
STARTINGSHOP={#mostly to skip intro, especially when enterting the room from a different starting location
  0x0145E4:bytes([0x00,0x48,0x87,0x46,0x00,0xC0,0x7F,0x08]),
  0x7FC000:bytes([0x01,0x20,0x40,0x22,0x12,0x02,0x10,0x43,0x07,0x4A,0x10,0x60,STARTINGSOUL[0],0x4A,0x01,0x20,0x07,0x32,0x10,0x70,STARTINGSOUL[1],0x4A,0x0F,0x20,0x10,0x70,0xCE,0x24,0xA4,0x00,0x0A,0x19,0xD0,0x20,0x04,0x4D,0xAF,0x46,0x00,0x00,0x40,0x03,0x00,0x02,0x1C,0x33,0x01,0x02,0x69,0x32,0x01,0x02,0xEC,0x45,0x01,0x08]),
}

def generate(generated):
  for address in STARTINGSHOP:
    generated.write(STARTINGSHOP[address],address)
