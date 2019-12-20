#tool to convert aa seqs to nt seqs using jcat's algorithm for codon usage with E.coli strain K12
#adapters are adapters used for ivtt pcr --- change if necessary
#input is csv
#outputs csv in directory with name, aa seq, and nt seq (with adapters)
#versions: V1,V2,V3, or B (for B cell)

import sys

complement = {'A':'T','T':'A','C':'G','G':'C'}
codon = {'M': 'ATG', 'S': 'TCT', 'P': 'CCG', 'V': 'GTT', 'N': 'AAC', 'L': 'CTG', 'C': 'TGC', 'I': 'ATC', 'Q': 'CAG', 'E': 'GAA', 'K': 'AAA', 'W': 'TGG', 'G': 'GGT', 'D': 'GAC', 'F': 'TTC', 'Y': 'TAC', 'H': 'CAC', 'A': 'GCT', 'T': 'ACC', 'R': 'CGT'}


def rev_comp(nt_seq):
    ls = []
    for nt in nt_seq:
        ls.append(complement[nt])
    ls.reverse()
    return ls


def aa_nt(pepfile, version):
    # outdir = str(pepfile).split('.')[0]
    # outfile = outdir+'_nt.csv'
    delim = ','

    #define ivtt pcr version
    if version == 'V2':
        #V2 adapters
        fp_adapter = "ATGGACGACGACGACAAG"
        tp_adapter = "TAACGAAGCACCTCGCTAAAAAAAAAAAAAAAAAAAAAAAAA"
    elif version == 'V3' or version == 'V1':
        #V1/V3 adapters
        fp_adapter = 'CGAGGTGCTTCGTTA'
        tp_adapter = 'CTTGTCGTCATCGTC'
    elif version == 'B':
        #B cell adapters
        fp_adapter = 'GAGCTTCGAAGATGTCGTTCAGACC'
        tp_adapter = 'CTTGTCGTCATCGTC'
    else:
        sys.exit('incorrect version id. Acceptable inputs are currently "V1", "V2", "V3", or "B"')

    # with open(pepfile) as f:
    #     f.write(','.join(['name','peptide','nt_seq'])+'\n')

    with open(pepfile,"r") as peptides:
        for line in peptides:
            line = line.replace('\n','')
            line = line.replace('\r','')
            line = line.split(delim)
            name = line[0]
            pep = line[1]
            nt = []
            for aa in pep:
                nt.append(codon[aa])
            nt = ''.join(nt)
            revcomp = rev_comp(nt)
            revcomp.insert(0,fp_adapter)
            revcomp.append(tp_adapter)
            revcomp = ''.join(revcomp)
            line = [name,pep,revcomp]
            with open('pepfile.txt') as f:
                f.write(','.join(line)+'\n')


