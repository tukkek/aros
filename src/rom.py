def read(rom,at,length=2):
  rom.seek(at)
  return rom.read(length)

def write(value,at,to):
  to.seek(at)
  to.write(value)

def copy(a,b,vanilla,generated,length=2):
  a=read(vanilla,a,length)
  write(a,b,generated)
