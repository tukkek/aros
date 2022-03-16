VERSION=open('version.txt').read()

def write(solver,filename):
  with open(filename+'.txt' ,'w') as spoilers:
    print('Version: '+VERSION,file=spoilers)
    print('Solution:',file=spoilers)
    for a in solver.actions:
      print('- '+a,file=spoilers)
