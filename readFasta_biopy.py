#!/usr/bin/env python

import sys
from Bio import SeqIO

for entry in SeqIO.parse(sys.argv[1],"fasta"):
    print entry.id
    print entry.seq
