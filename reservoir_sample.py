#!/usr/bin/env python2.7
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

import argparse
p = argparse.ArgumentParser()
p.add_argument('sample_size', type=float)
p.add_argument('input_file', nargs='?')
p.add_argument('--shuffle', action='store_true', help="Shuffle the final output (otherwise order is not totally random, esp if input file is small)")
args = p.parse_args()

if args.input_file:
    input = open(args.input_file, 'r')
else:
    input = sys.stdin

N = int(args.sample_size)
sample = []

for i,line in enumerate(input):
    if i < N:
        sample.append(line)
    elif i >= N and random.random() < N/(i+1):
        replace = random.randint(0, len(sample)-1)
        sample[replace] = line

if args.shuffle:
    random.shuffle(sample)

for line in sample:
    sys.stdout.write(line)
