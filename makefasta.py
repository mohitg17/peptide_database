from __future__ import print_function
import sys

#V2 adapters
fp_adapter = "ATGGACGACGACGACAAG"
tp_adapter = "TAACGAAGCACCTCGCTAAAAAAAAAAAAAAAAAAAAAAAAA"


def makefasta(filein):
    with open(filein, "r") as f:
        next(f)
        for line in f:
            line = line.replace('\n','')
            line = line.replace('\r','')
            line = line.split('\t')
            nt = str(line[2])
            name = str(line[0])
            pep = str(line[1])
            nt = nt.replace(fp_adapter)
            nt = nt.replace(tp_adapter)
            print('>'+name+': '+pep+'\n'+nt)

#END
