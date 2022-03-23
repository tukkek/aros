class Rom:
  def __init__(self,gba):
    self.gba=gba

  def read(self,at,length=2):
    self.gba.seek(at)
    return self.gba.read(length)

  def write(self,value,at):
    self.gba.seek(at)
    self.gba.write(value)

  def copy(self,a,b,rom,length=2):
    rom.write(self.read(a,length),b)

  def readint(self,at,length=2):
    return int.from_bytes(self.read(at,length),byteorder='little')

  def writeint(self,i,at,length=2):
    self.write(int(i).to_bytes(length,byteorder='little'),at)
