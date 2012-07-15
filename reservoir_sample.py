#!/usr/bin/env python
#
# The reservoir sampling algorithm outputs a sample of N lines from a
# file of undetermined size. It does so in a single pass, using memory
# proportional to N.  These two features -- (i) a constant memory
# footprint and (ii) a capacity to operate on files of indeterminate
# size -- make it ideal for working with very large data sets common
# to event processing.
#
# adapted from https://github.com/dataspora/big-data-tools/blob/master/samplen.py
#
from __future__ import division
import sys
import random

if len(sys.argv) == 3:
    input = open(sys.argv[2],'r')
elif len(sys.argv) == 2:
    input = sys.stdin
else:
    print "Usage:  python samplen.py <num lines> <?file, else stdin>"
    sys.exit(1)

N = int(float(sys.argv[1]))
sample = []

for i,line in enumerate(input):
    if i < N:
        sample.append(line)
    elif i >= N and random.random() < N/(i+1):
        replace = random.randint(0, len(sample)-1)
        sample[replace] = line

for line in sample:
    sys.stdout.write(line)
