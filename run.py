#!/usr/bin/python3
import progression,solver

s=solver.Solver(progression.CORRIDOR,solver.VANILLAREWARDS)
print('Success!' if s.solve() else 'Failure...')
print()
print('Log:')
for a in s.actions:
  print('- '+a)
