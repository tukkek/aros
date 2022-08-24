#TODO joining teleporter rooms together would be a long term goal for extra routing possibilities?
import progression,args

DEBUG=None
ADDRESS=0x004F0D8C
VALUES={
  progression.CHAPEL:bytes([0x01,0x0E]),
  progression.STUDY:bytes([0x02,0x0C]),
  progression.HALL:bytes([0x03,0x15]),
  progression.QUARTERS:bytes([0x04,0x14]),
  progression.GARDEN:bytes([0x05,0x0C]),
  progression.TOWER:bytes([0x06,0x0F]),
  progression.RESERVOIR:bytes([0x07,0x27]),
  progression.ARENA:bytes([0x08,0x15]),
  progression.TOP:bytes([0x09,0x16])
}

def generate(solver,generated):
  entrance=(args.debug and DEBUG) or solver.progress[0]
  if entrance!=progression.CORRIDOR:
    generated.write(VALUES[entrance],ADDRESS)
