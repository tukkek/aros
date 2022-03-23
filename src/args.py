import argparse,time

rom='rom.gba'
debug=False
seed=int(time.time())

instructions={
  'rom':f'Defaults to "{rom}".',
  'seed':'Number or text to be used as RNG seed.',
  'debug':'If used, a testing-friendly ROM will be created. Will overwrite -seed with "debug"',
}

def setup():
  global rom,debug,seed
  p=argparse.ArgumentParser()
  p.add_argument('--rom',default=rom,help=instructions['rom'])
  p.add_argument('--seed',default=seed,help=instructions['seed'])
  p.add_argument('--debug',default=debug,action='store_true',help=instructions['debug'])
  p=vars(p.parse_args())
  rom=p['rom']
  debug=p['debug']
  seed='debug' if debug else p['seed']

setup()
