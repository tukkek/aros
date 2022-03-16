import argparse,time

rom='rom.gba'
debug=False
seed=int(time.time())

def setup():
  global rom,debug,seed
  p=argparse.ArgumentParser()
  p.add_argument('--rom',default=rom,help='Defaults to: '+rom)
  p.add_argument('--debug',default=debug,action='store_true',help='If used, a testing-friendly ROM will be created')
  p.add_argument('--seed',default=seed,help='Number or text to be used as RNG seed')
  p=vars(p.parse_args())
  rom=p['rom']
  debug=p['debug']
  seed=p['seed']

setup()
