#tool to convert aa seqs to nt seqs using jcat's algorithm for codon usage with E.coli strain K12
#adapters are adapters used for ivtt pcr --- change if necessary
#input is csv
#outputs csv in directory with name, aa seq, and nt seq (with adapters)
#versions: V1,V2,V3, or B (for B cell)

import sys
import pandas as pd

complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
codon = {'M': 'ATG', 'S': 'TCT', 'P': 'CCG', 'V': 'GTT', 'N': 'AAC', 'L': 'CTG', 'C': 'TGC', 'I': 'ATC',
         'Q': 'CAG', 'E': 'GAA', 'K': 'AAA', 'W': 'TGG', 'G': 'GGT', 'D': 'GAC', 'F': 'TTC', 'Y': 'TAC',
         'H': 'CAC', 'A': 'GCT', 'T': 'ACC', 'R': 'CGT'}


def aa_nt(pepfile, ntfile, version):
    # define ivtt pcr version
    if version == 'V2':
        fp_adapter = "ATGGACGACGACGACAAG"
        tp_adapter = "TAACGAAGCACCTCGCTAAAAAAAAAAAAAAAAAAAAAAAAA"
    elif version == 'V3' or version == 'V1':
        fp_adapter = 'CGAGGTGCTTCGTTA'
        tp_adapter = 'CTTGTCGTCATCGTC'
    elif version == 'B':
        fp_adapter = 'GAGCTTCGAAGATGTCGTTCAGACC'
        tp_adapter = 'CTTGTCGTCATCGTC'
    else:
        sys.exit('incorrect version id. Acceptable inputs are currently "V1", "V2", "V3", or "B"')

    # read source csv
    df = pd.read_csv(pepfile)
    names = df.name
    pep_seq = df.peptide_seq
    nt_seqs = []
    revcomp = []

    # translate pep_seq to nt_seq and generate revcomp using nt_seq
    for i in range(len(pep_seq)):
        # translate pep_seq to nt_seq
        nt_seq = ""
        for aa in pep_seq[i]:
            nt_seq += codon[aa]
        nt_seqs.append(nt_seq)
        pd.Series(nt_seqs)

        # generate revcomp
        rev = nt_seq[::-1]
        table = str.maketrans(complement)
        # add adapters
        comp = fp_adapter + rev.translate(table) + tp_adapter
        revcomp.append(comp)
        pd.Series(revcomp)

    frame = {'name' : names, 'pep_seq' : pep_seq, 'nt_seq' : nt_seqs, 'revcomp' : revcomp}
    result = pd.DataFrame(frame)

    # output to csv
    result.to_csv(path_or_buf=ntfile, index=False)