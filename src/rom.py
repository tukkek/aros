def read(rom,at,length=2):
  rom.seek(at)
  return rom.read(length)

def write(value,at,rom):
  rom.seek(at)
  rom.write(value)

def copy(a,b,vanilla,generated,length=2):
  a=read(vanilla,a,length)
  write(a,b,generated)

def readint(at,rom,length=2):
  return int.from_bytes(read(rom,at,length),byteorder='little')

def writeint(i,at,rom,length=2):
  write(int(i).to_bytes(length,byteorder='little'),at,rom)
